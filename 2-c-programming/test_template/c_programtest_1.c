#include <stdio.h>
#include "c_programtest_1.h"
// these functions are related to 2.02-2.07 :::: data types, syntax, variables, conditionals and operators.
// You must review through functions (2.07) first to complete these tests.


//Data Type to use:   short integer, short integer, int.
//Instruction:  Complete this function.  The function should accept a  integer as
//parameter.  Create a new short integer variable short_n, and assign the value of n to short_n.  Then, reverse by assigning the value of short_n to n. return n.
// What is the practical consequence of this function depending on input?
//test_1 is the function name
 short test_1(int n)
{

    short short_n = n;
    n= short_n;
    return n;
}

//Data Type to use:  unsigned integer, bool. Conditionals: if, and, not.  Operator:  modulus
//This function will acccept an unsigned int and bool.  You will extract a boolean value
// by  testing for even or odd number (assume only positive values) and then the boolean
//variable will be used in an expression to generate a final boolean return value.
//Instructions: Declare bool variable x and intialize to false.  
//Assign true if input n is even. Write a single line boolean expression in a return statement 
//that returns the opposite value of "x (logical AND) i," also known as NAND operation.
//test_2 is the function name
bool test_2(unsigned int n, bool i)
{
  bool x = false;
  if (n % 2 == 0 )
  {
     x = true;
  }
  return (!(x && i));
}


//test_3 is the function name
//write a function to accepts a char and determines whether it is valid lower case or upper case
//Return bool true if valid letter except for letter 'X' which is dangerous to the calling
//program.  Return false for 'X' (upper) and all other ascii values. Do not use any character related 
//libraries or functions.  Only use operators and conditionals presented in these TTG-B sections.
bool test_3(char input)
{

  if (((65 <= input) && (input<= 90)) || ((97 <= input) && (input <= 122)))
  {
     if (input != 88) //could be added to line above.  here for clarity
     {
     return true;
     }
  }
  return (false);
}

//am_i_prime is function name
// write a function that accepts an unsigned int and returns true if it is prime and less than 
//1000 or false otherwise.  Input is can be any unsigned int including zero. zero is not a prime 
//(nor is 1). Protect your code from dividing by zero! Do not use any other function or library.
//try to limit the computation time with a smart function. Do not  google anything.  
//A prime number is only divisible by 1 and itself (divisible with remainder zero).

bool am_i_prime(unsigned num)
{
  if (num >=1000)
  {
    return false;
 
  }
  if ((num==0) || (num == 1) || (num ==2))
  {
  return false;
  } 
  unsigned int max_divisor = num / 2;
  for (unsigned int i = 2; i < max_divisor; i++) //would be better to limit to sqaure root of num, but not in TTG-B
  {
     if ((num % i) == 0)
     {

        return false;
     }  
  }   
 
  return (true);
}





