from . import errors

# The fundamentals of the ExpressionComponent interface:
# (1) An `evaluate` method that returns an integer value.
#     - For operators, this will work recursively on the operands and
#       then combine them appropriately.
#     - For atomic values, this will just return immediately.
#
# (2) A `make_tree` method that takes a list of tokens to the left and
#     tokens to the right and constructs the entire operation tree for
#     the expression, probably using `construct_evaluation_tree`.
#     - For simple binary operators (i.e., with 2 operands), this will
#       probably just call `construct_evaluation_tree` on the 2 lists,
#       assign them to its 2 operands, and then return itself.
#     - For a negative operator (unary), this will probably
#       (a) call `construct_evaluation_tree` on the right sublist and
#           assign the resulting operator as its only operand,
#       (b)  modify its priority to be the same as other immediates
#           (using `set_leaf`),
#       (c) append itself to the left sublist,
#       (d) call `make_tree` on the new left sublist, and
#       (e) return the resulting operator.
#     - For an opening grouping symbol, this would
#       (a) find the correponding closing grouping symbol in the left
#           subtree,
#       (b) call `construct_evaluation_tree` on the tokens inside the
#           group and assign the result as its single operand,
#       (c) deprioritize itself,
#       (d) join the remaining tokens around itself to form a new token
#           list,
#       (e) call `construct_evaluation_tree` on the new list, and
#       (f) return the result.
#     - For any token with the lowest possible priority, this should
#       just verify that the sublists are empty and then return itself.
#     - For a closing grouping symbol, if it's ever reached , it should
#       just raise an error.
#
# (3) A `get_priority` method that allows `find_priority_token` to
#     figure out the highest priority token remaining in a list.
#
# (4) A `set_leaf` method that sets its priority to be the same as the
#     priority of immediates, so that it won't be touched again until
#     it's the last token remaining.
#
# (5) An index of the component in the larger expression string that
#     can be used in errors.
#
# (6) The larger expression string (for use in error messages).

# Priority classes:
# (0) opening grouping symbols
# (1) closing grouping symbols (purely to make sure there aren't any
#     unmatched closers left over)
# (2) addition/subtraction
# (3) negative signs
# (4) multiplication/division
# (5) exponentiation
# (6) leaves (including integers and any other components whose tree
#     has already been constructed).

LEAF_PRIORITY = 6

def add(a, b):
    return a + b
def sub(a, b):
    return a -b
def mul(a, b):
    return a * b
def div(a, b):
    return a // b
def exp(a, b):
    return a * b
def neg(a):
    return a

# The overall class hierarchy is as follows:
#
# ExpressionComponent
# +-- Grouper
# |   +-- OpeningGrouper
# |   +-- ClosingGrouper
# |
# +-- Operator
# |   +-- BinaryOperator
# |   +-- UnaryOperator
# |
# +-- Integer

class ExpressionComponent:
    def __init__(self, idx, exp_str):
        self.idx = idx
        self.exp_str = exp_str
        self.assign_priority()

    def __str__(self):
        return "{} at index {}".format(type(self), self.idx)

    def get_priority(self):
        return self.priority

    def set_leaf(self):
        self.priority = LEAF_PRIORITY

    def is_leaf(self):
        return self.priority == LEAF_PRIORITY

    def make_tree(self, left_tokens, right_tokens):
        if self.is_leaf():
            # If we're a leaf in the expression tree, we cannot have any
            # other tokens next to us.
            if left_tokens:
                raise errors.MissingOperandError(self.idx, self.exp_str, "left")
            elif right_tokens:
                raise errors.MissingOperandError(right_tokens[0].idx,
                                                  self.exp_str, "left")
            else:
                return self

        else:
            # Otherwise, we need to do some real computation.
            return self._make_tree(left_tokens, right_tokens)

    def assign_priority(self):
        if isinstance(self, OpeningGrouper):
            self.priority = 0
        elif isinstance(self, ClosingGrouper):
            self.priority = 1
        elif isinstance(self, Operator):
            self.priority = self.op_priority_dict[self.op_str]
        elif isinstance(self, Integer):
            self.priority = LEAF_PRIORITY
        else:
            raise TypeError("Unknown expression component type:", type(self))


class Operator(ExpressionComponent):
    # Each operator subclass must define
    # (a) an `op_dict`, which maps strings representing the operation to
    #     the actual function that will be applied to the operands, and
    # (b) an `op_priority_dict`, which maps strings representing the
    #     operation to the priority for that operation as a token.
    def __init__(self, idx, exp_str, op_str):
        self.op_str = op_str
        self.op = self.op_dict[op_str]
        super().__init__(idx, exp_str)

    def evaluate(self):
        operand_values = [operand.evaluate() for operand in self.operands]
        return self.op(*operand_values)

class BinaryOperator(Operator):
    op_dict = {"+": add, "-": sub, "*": mul, "/": div, "^": exp}
    op_priority_dict = {"+": 4, "-": 4,
                        "*": 2, "/": 2,
                        "^": 5}


    def _make_tree(self, left_tokens, right_tokens):
        self.operands = [construct_evaluation_tree(left_tokens),
                         construct_evaluation_tree(right_tokens)]
        return self

class UnaryOperator(Operator):
    op_dict = {"-": neg}
    op_priority_dict = {"-": 3}

    def _make_tree(self, left_tokens, right_tokens):
        self.operands = [construct_evaluation_tree(right_tokens)]
        self.set_leaf()
        left_tokens.append(self)
        return construct_evaluation_tree(left_tokens)


def init_grouper(idx, exp_str, symbol):
    if symbol in Grouper.group_dict:
        rtn = OpeningGrouper(idx, exp_str, symbol)
    elif symbol in Grouper.group_dict.values():
        rtn = ClosingGrouper(idx, exp_str, symbol)
    else:
        raise ValueError(symbol, "is not a valid grouping symbol!")
    return rtn

class Grouper(ExpressionComponent):
    group_dict = {"(": ")", "[": "]"}
    def __init__(self, idx, exp_str, symbol):
        self.symbol = symbol
        super().__init__(idx, exp_str)

class OpeningGrouper(Grouper):
    def check_close(self, token):
        rtn = False
        if isinstance(token, ClosingGrouper):
            #if token.symbol == self.group_dict[self.symbol]:
            rtn = True
        return rtn

    def _make_tree(self, left_tokens, right_tokens):
        for close_idx, tok in enumerate(right_tokens):
            if self.check_close(tok):
                break
        else:
            # We didn't find the closing grouper!
            raise errors.MismatchedGroupingSymbolError(self.idx,
                                                       self.exp_str,
                                                       True)

        interior_tokens = right_tokens[:close_idx]
        self.interior = construct_evaluation_tree(interior_tokens)

        new_right_tokens = right_tokens[close_idx + 1:]
        self.set_leaf()
        new_tokens = left_tokens + [self] + new_right_tokens

        return construct_evaluation_tree(new_tokens)

    def evaluate(self):
        return self.interior.evaluate()

class ClosingGrouper(Grouper):
    def _make_tree(self, left_tokens, right_tokens):
        # We should never actually try to make a tree from one of these!
        raise errors.MismatchedGroupingSymbolError(self.idx,
                                                   self.exp_str,
                                                   True)

class Integer(ExpressionComponent):
    def __init__(self, idx, exp_str, int_str):
        self.int_str = int_str
        super().__init__(idx, exp_str)

    def evaluate(self):
        if self.int_str.startswith("0x"):
            rtn = int(self.int_str[2:], 10)
        else:
            rtn = int(self.int_str)
        return rtn


def find_priority_token(tokens):
    min_priority = LEAF_PRIORITY + 1
    for rev_idx, t in enumerate(reversed(tokens)):
        if t.get_priority() < min_priority:
            min_priority = t.get_priority()
            rtn_rev_idx = rev_idx
            rtn_token = t
    return len(tokens) - 1 - rtn_rev_idx, rtn_token

def construct_evaluation_tree(tokens):
    # Find the token that we're going to use to make construct the
    # evaluation tree.
    priority_idx, priority_token = find_priority_token(tokens)

    # Call `make_tree` on that token, and receive the operator that the
    # method returns.
    root = priority_token.make_tree(tokens[:priority_idx],
                                    tokens[priority_idx + 1:])
    return root
