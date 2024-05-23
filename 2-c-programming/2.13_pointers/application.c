#include <stdio.h>
#include <stdlib.h>

int main(){
    int x = 10;

    //TODO:: Create a pointer that points to x. 
    
    //TODO:: Call the passByValueFunction, giving it x as an argument. Print the value of x after the function returns.

    //TODO:: Call the passByPtrFunction, giving it the pointer to x as an argument. Print the value of x after the function returns.


    return 0;
}

void passByValueFunction(int x){
    x = 70;
}

void passByPtrFunction(int* ptr){
    *ptr = 20;
}
