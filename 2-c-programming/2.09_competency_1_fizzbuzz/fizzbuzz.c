#include <stdio.h>
#include "cs50.h"

void fizzBuzz(int n) {
    // TODO: This function should print the following:
    //       Fizz for numbers divisible by 3,
    //       Buzz for numbers divisible by 5, 
    //       FizzBuzz for numbers divisible by both 3 and 5,
    //       and the number itself for all other cases.
    for (int i = 0; i <= n; i++) {
        if (i % 3 == 0) printf("Fizz");
        if (i % 5 == 0) printf("Buzz");
        if (i % 3 != 0 && i % 5 != 0) printf("%d", i);
        printf("\n");
    }


}

int main() {

    // TODO: Prompt the user to enter a number using get_int() and store it in the variable 'num'

    // TODO: Call fizzBuzz() in a loop from 1 to the number that the user has entered as the parameter.
    // Example: if the user entered 20, fizzBuzz() should run for every number between 1 to 20.
    int num = get_int("Input: ");
    fizzBuzz(num);
    return 0;
}
