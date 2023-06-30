# Python Operators

[Back to README](README.md)

Operators are the constructs, which can manipulate the value of operands. Consider the expression 4 + 5 = 9. Here, 4 and 5 are called the operands and + is called the operator.

Types of Operator
-----------------

Python language supports the following types of operators −

*   Arithmetic Operators
*   Comparison (Relational) Operators
*   Assignment Operators
*   Logical Operators
*   Bitwise Operators
*   Membership Operators
*   Identity Operators

Let us have a look at all the operators one by one.

Python Arithmetic Operators
---------------------------

Assume variable **a** holds the value 10 and variable **b** holds the value 21, then −

[Show Example](https://www.tutorialspoint.com/python3/arithmetic_operators_example.htm)



* Operator: + Addition
  * Description: Adds values on either side of the operator.
  * Example: a + b = 31
* Operator: - Subtraction
  * Description: Subtracts right hand operand from left hand operand.
  * Example: a – b = -11
* Operator: * Multiplication
  * Description: Multiplies values on either side of the operator
  * Example: a * b = 210
* Operator: / Division
  * Description: Divides left hand operand by right hand operand
  * Example: b / a = 2.1
* Operator: % Modulus
  * Description: Divides left hand operand by right hand operand and returns remainder
  * Example: b % a = 1
* Operator: ** Exponent
  * Description: Performs exponential (power) calculation on operators
  * Example: a**b =10 to the power 20
* Operator: //
  * Description: Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity):
  * Example: 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0


Python Comparison Operators
---------------------------

These operators compare the values on either side of them and decide the relation among them. They are also called Relational operators.

Assume variable **a** holds the value 10 and variable **b** holds the value 20, then −

[Show Example](https://www.tutorialspoint.com/python3/comparison_operators_example.htm)



* Operator: ==
  * Description: If the values of two operands are equal, then the condition becomes true.
  * Example: (a == b) is not true.
* Operator: !=
  * Description: If values of two operands are not equal, then condition becomes true.
  * Example: (a!= b) is true. 
* Operator: >
  * Description: If the value of left operand is greater than the value of right operand, then condition becomes true.
  * Example: (a > b) is not true.
* Operator: <
  * Description: If the value of left operand is less than the value of right operand, then condition becomes true.
  * Example: (a < b) is true.
* Operator: >=
  * Description: If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.
  * Example: (a >= b) is not true.
* Operator: <=
  * Description: If the value of left operand is less than or equal to the value of right operand, then condition becomes true.
  * Example: (a <= b) is true.


Python Assignment Operators
---------------------------

Assume variable **a** holds the value 10 and variable **b** holds the value 20, then −

[Show Example](https://www.tutorialspoint.com/python3/assignment_operators_example.htm)



* Operator: =
  * Description: Assigns values from right side operands to left side operand
  * Example: c = a + b assigns value of a + b into c
* Operator: += Add AND
  * Description: It adds right operand to the left operand and assign the result to left operand
  * Example: c += a is equivalent to c = c + a
* Operator: -= Subtract AND
  * Description: It subtracts right operand from the left operand and assign the result to left operand
  * Example: c -= a is equivalent to c = c - a
* Operator: *= Multiply AND
  * Description: It multiplies right operand with the left operand and assign the result to left operand
  * Example: c *= a is equivalent to c = c * a
* Operator: /= Divide AND
  * Description: It divides left operand with the right operand and assign the result to left operand
  * Example: c /= a is equivalent to c = c / ac /= a is equivalent to c = c / a
* Operator: %= Modulus AND
  * Description: It takes modulus using two operands and assign the result to left operand
  * Example: c %= a is equivalent to c = c % a
* Operator: **= Exponent AND
  * Description: Performs exponential (power) calculation on operators and assign value to the left operand
  * Example: c **= a is equivalent to c = c ** a
* Operator: //= Floor Division
  * Description: It performs floor division on operators and assign value to the left operand
  * Example: c //= a is equivalent to c = c // a


Python Bitwise Operators
------------------------

Bitwise operator works on bits and performs bit-by-bit operation. Assume if a = 60; and b = 13; Now in binary format they will be as follows −

a = 0011 1100

b = 0000 1101

\-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a = 1100 0011

Python's built-in function bin() can be used to obtain binary representation of an integer number.

The following Bitwise operators are supported by Python language −

[Show Example](https://www.tutorialspoint.com/python3/bitwise_operators_example.htm)



* Operator: & Binary AND
  * Description: Operator copies a bit, to the result, if it exists in both operands
  * Example: (a & b) (means 0000 1100)
* Operator: | Binary OR
  * Description: It copies a bit, if it exists in either operand.
  * Example: (a | b) = 61 (means 0011 1101)
* Operator: ^ Binary XOR
  * Description: It copies the bit, if it is set in one operand but not both.
  * Example: (a ^ b) = 49 (means 0011 0001)
* Operator: ~ Binary Ones Complement
  * Description: It is unary and has the effect of 'flipping' bits.
  * Example: (~a ) = -61 (means 1100 0011 in 2's complement form due to a signed binary number.
* Operator: << Binary Left Shift
  * Description: The left operand's value is moved left by the number of bits specified by the right operand.
  * Example: a << 2 = 240 (means 1111 0000)
* Operator: >> Binary Right Shift
  * Description: The left operand's value is moved right by the number of bits specified by the right operand.
  * Example: a >> 2 = 15 (means 0000 1111)


Python Logical Operators
------------------------

The following logical operators are supported by Python language. Assume variable **a** holds True and variable **b** holds False then −

[Show Example](https://www.tutorialspoint.com/python3/logical_operators_example.htm)



* Operator: and Logical AND
  * Description: If both the operands are true then condition becomes true.
  * Example: (a and b) is False.
* Operator: or Logical OR
  * Description: If any of the two operands are non-zero then condition becomes true.
  * Example:  (a or b) is True.
* Operator: not Logical NOT
  * Description: Used to reverse the logical state of its operand.
  * Example: Not(a and b) is True.


Python Membership Operators
---------------------------

Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples. There are two membership operators as explained below −

[Show Example](https://www.tutorialspoint.com/python3/membership_operators_example.htm)



* Operator: in
  * Description: Evaluates to true if it finds a variable in the specified sequence and false otherwise.
  * Example: x in y, here in results in a 1 if x is a member of sequence y.
* Operator: not in
  * Description: Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.
  * Example: x not in y, here not in results in a 1 if x is not a member of sequence y.


Python Identity Operators
-------------------------

Identity operators compare the memory locations of two objects. There are two Identity operators as explained below −

[Show Example](https://www.tutorialspoint.com/python3/identity_operators_example.htm)



* Operator: is
  * Description: Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
  * Example: x is y, here is results in 1 if id(x) equals id(y).
* Operator: is not
  * Description: Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.
  * Example: x is not y, here is not results in 1 if id(x) is not equal to id(y).


Python Operators Precedence
---------------------------

The following table lists all operators from highest precedence to the lowest.

[Show Example](https://www.tutorialspoint.com/python3/operators_precedence_example.htm)


|Sr.No.|Operator & Description                                                             |
|------|-----------------------------------------------------------------------------------|
|1     |**Exponentiation (raise to the power)                                              |
|2     |~ + -Complement, unary plus and minus (method names for the last two are +@ and -@)|
|3     |* / % //Multiply, divide, modulo and floor division                                |
|4     |+ -Addition and subtraction                                                        |
|5     |>> <<Right and left bitwise shift                                                  |
|6     |&Bitwise 'AND'                                                                     |
|7     |^ |Bitwise exclusive `OR' and regular `OR'                                         |
|8     |<= < > >=Comparison operators                                                      |
|9     |<> == !=Equality operators                                                         |
|10    |= %= /= //= -= += *= **=Assignment operators                                       |
|11    |is is notIdentity operators                                                        |
|12    |in not inMembership operators                                                      |
|13    |not or andLogical operators                                                        |
