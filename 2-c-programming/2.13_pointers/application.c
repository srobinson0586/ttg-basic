#include <stdio.h>
#include <stdlib.h>

int main(){
    int x = 10;
    //TODO:: create a pointer that points to x 
    
    //TODO:: call passByValueFunction and print the value of x

    //TODO::call passByPtrFunction and print the value of x


    
    return 0;
}
void passByPtrFunction(int* ptr){
    *ptr = 20;
}
void passByValueFunction(int ptr){
    ptr = 20;
}