from . import components
from . import errors

grouping_symbols = set(components.Grouper.group_dict.keys())
grouping_symbols.update(components.Grouper.group_dict.values())

def is_hex_digit(c):
    hex_letters = {"a", "b", "c", "d", "e", "f"}
    if c.isdigit() or c in hex_letters:
        rtn = True
    else:
        rtn = False
    return rtn

def is_decimal_digit(c):
    return c.isdigit()

class Expression:
    def __init__(self, string):
        self.string = string
        self.current_idx = 0
        ### We'll use this flag to determine if "-" characters are
        ### subtraction operators or negative signs.
        self.dash_as_neg = True

    def __str__(self):
        return self.string

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, idx):
        return self.string[idx]

    def getchar(self):
        return self[self.current_idx]

    def inc(self):
        self.current_idx += 1

    def get_next_token(self):
        """ Find the next token in `expression`, starting at index `idx`.

        If there is a next token, return the next token.
        Return None if we reach the end of the expression without
        finding another token (i.e., if the rest is whitespace).
        Raise an ExpressionError if the next token is improperly
        formatted.

        Update self.current_idx to point to the next character to be
        parsed.

        This only tokenizes the string; it helps create a list of the
        tokens in the order they appear in the string. The order of
        operations comes into effect only when evaluate() is called.
        """

        ### First, find the first non-whitespace character.
        rtn = ""
        while True:
            if self.current_idx == len(self.string):
                ### There are no more non-white characters, so there is
                ### no next token.
                rtn = None
                break
            elif self.getchar().isspace():
                self.inc()
            else:
                break

        ### Now figure out the actual ExpressionComponent for the next
        ### token.
        if rtn is not None:
            if self.getchar() in components.BinaryOperator.op_dict:
                ### The next token is an binary operation or a negative
                ### sign.
                if self.getchar() == "-" and self.dash_as_neg:
                    rtn = components.UnaryOperator(self.current_idx,
                                                   self.string,
                                                   self.getchar())
                else:
                    rtn = components.BinaryOperator(self.current_idx,
                                                    self.string,
                                                    self.getchar())
                self.inc()

            elif self.getchar().isdigit():
                ### The next token is a number.
                start_idx = self.current_idx

                # If there's a hex prefix, skip past it.
                if self.string[self.current_idx:].startswith("0x"):
                    is_digit = is_hex_digit
                    self.inc()
                    self.inc()
                else:
                    is_digit = is_decimal_digit

                while True:
                    if self.current_idx == len(self.string):
                        break
                    elif not is_digit(self.getchar()):
                        break
                    else:
                        self.inc()
                rtn = components.Integer(start_idx, self.string,
                                         self[start_idx: self.current_idx])

            elif self.getchar() in grouping_symbols:
                rtn = components.init_grouper(self.current_idx,
                                              self.string,
                                              self.getchar())
                self.inc()

            else:
                raise errors.UnexpectedCharacterError(0,
                                                      self.string)

        ### Indicate whether we found an operator so we can continue
        ### classifying "-"s appropriately.
        self.dash_as_neg = (isinstance(rtn, components.Operator) or
                            isinstance(rtn, components.OpeningGrouper))

        return rtn

    def get_tokens(self):
        tokens = []
        while True:
            next_token = self.get_next_token()
            if next_token is None:
                break
            tokens.append(next_token)
        return tokens

    def evaluate(self):
        tokens = self.get_tokens()
        root = components.construct_evaluation_tree(tokens)
        return root.evaluate()


def evaluate(expression):
    """ Evaluate `expression` as an arithmetic expression. """
    e = Expression(expression)
    return e.evaluate()

if __name__ == "__main__":
    print(evaluate("(4 + 2) * --3 * [-4 + (-2^3)]"))
