class ExpressionError(BaseException):
    """ The base class for malformed expression errors

    All ExpressionErrors have an `idx` attribute that identifies the index
    of the error in the overall expression string. """

    def __init__(self, summary, idx, exp_str):
        self.idx = idx
        self.exp_str = exp_str
        sub_str = " " * idx + "^"
        self.msg = "\n".join([summary, exp_str, sub_str])
        super().__init__(self.msg)

    def __str__(self):
        return self.msg


class MismatchedGroupingSymbolError(ExpressionError):
    """ The class for errors caused by mismatched grouping symbols

    This error class is raised if there is a grouping symbol that does not
    have an appropriate match.

    Attributes:
    - `idx` is the index of the mismatched grouping symbol.
    - `kind` (either "opening" or "closing") indicates whether the mismatched
      symbol was an opening or closing grouping symbol. """

    def __init__(self, idx, exp_str, closing):
        if closing:
            self.kind = "closing"
        else:
            self.kind = "opening"
        summary = "Mismatched {} grouping symbol at index {}"
        summary = summary.format(self.kind, idx)
        super().__init__(summary, idx, exp_str)

class MissingOperatorError(ExpressionError):
    """ The class for errors caused by missing operators

    This error class is raised if the parser detects 2 adjacent expressions
    that are not separated by an operator.

    Attributes:
    - `idx` is the index of the 2nd adjacent expression. """

    def __init__(self, idx, exp_str):
        summary = "Missing operator at index {}".format(idx)
        super().__init__(summary, idx, exp_str)

class MissingOperandError(ExpressionError):
    """ The class for errors caused by missing operands

    This error class is raised if the parser detects an operator (unary
    or binary) that is missing one of its operands.

    Attributes:
    - `idx` is the index of the operator.
    - `operand_side` (either "left" or "right") indicates the side the
      missing operand should be on. """

    def __init__(self, idx, exp_str, operand_side):
        self.operand_side = operand_side
        summary = "Operator at index {} is missing {} operand"
        summary = summary.format(idx, operand_side)
        super().__init__(summary, idx, exp_str)

class UnexpectedCharacterError(ExpressionError):
    """ The class for errors caused by unexpected characters

    This error class is raised if the interpreter cannot parse a character
    in the expression (for example, if it finds a letter in the middle of a
    decimal integer).

    Attributes:
    - `idx` is the index of the unexpected character. """

    def __init__(self, idx, exp_str):
        summary = "Unepected character at index {}".format(idx)
        super().__init__(summary, idx, exp_str)

class EmptyExpressionError(ExpressionError):
    """ The class for errors caused by empty expressions

    This error class is raised if the parser encounters an empty expression.
    There are 2 cases where this can happen:
    A. The entire expression is empty (or contains only whitespace).
    B. The expression contains a pair of grouping symbols containing nothing
       (or only whitespace).

    Attributes:
    - `idx`
      - For case A, `idx` is 0.
      - For case B, `idx` is the index of the opening grouping symbol. """

    def __init__(self, idx, exp_str):
        summary = "Empty expression at index {}".format(idx)
        super().__init__(summary, idx, exp_str)
