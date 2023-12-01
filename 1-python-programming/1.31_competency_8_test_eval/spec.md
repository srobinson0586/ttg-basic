# Specification for `expression.py`

[Return to Competency 8 Assignment](README.md)

## Expression format

The simplest kind of expression is a single integer. Integers can be
written in decimal (with no prefix) or hexadecimal (with a "0x" prefix
and all lowercase hex letters).

More complex expressions can be constructed according to these rules:
1. An expression surrounded by arbitrary whitespace is a valid expression.

2. An expression surrounded by parentheses ("()") or square brackets
   ("[]") is a valid expression.

3. An expression preceeded by a unary operator is a valid expression.
   The valid unary operators are: 
   - Negation ("-")

4. Two expressions joined by a binary operator is a valid expression.
   The valid binary operators are:
   - Addition ("+")
   - Subtraction ("-")
   - Multiplication ("*")
   - Division ("/")
   - Exponentiation ("^")

## Expression Evaluation

Expressions are evaluated according to the standard order of operations:
1. Expressions in parentheses are evaluated as a unit
2. Exponentiation
3. Mulitplication and division
4. Addition and subtraction

Division is always integer division (notated in Python3 with "//").


## Errors

The following errors are raised when evaluating an invalid expression (if
an expression has multiple issues, any appropriate error may be raised):
1. MismatchedGroupingSymbolError

2. MissingOperatorError

3. MissingOperandError

4. UnexpectedCharacterError

5. EmptyExpressionError

See the docstrings in [`expression/errors.py`](./expression/errors.py) for
detailed information about each error class.

[Return to Competency 8 Assignment](README.md)
