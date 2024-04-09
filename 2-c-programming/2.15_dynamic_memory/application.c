#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr = NULL;
    int n;

    // TODO: Step 1 - Allocate memory for an array of 10 integers using malloc and store it in *ptr. Store the number of elements in n.
    
    if (ptr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // TODO: Step 2 - Free the dynamically allocated memory using free and set it to NULL

    if (ptr == NULL) {
        printf("Memory freed successfully.\n");
    }

    // TODO: Step 3 - Allocate and Initialize an array of 10 elements to zero using calloc. Store array in *ptr
   
    if (ptr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    for(int i = 0; i<10;i++){
        if(ptr[i] != 0){
            printf("Memory initialization failed!\n");
            return 1;
        }
    }

    // TODO: Step 4 - Modify the size of the array using realloc to 15 elements and assign the last element to 27

    if (ptr == NULL) {
        printf("Memory reallocation failed!\n");
        return 1;
    }
    if(ptr[14]!= 27){
         printf("Memory reallocation failed!\n");
        return 1;
    }

    // Display the reallocated memory
    printf("Memory reallocated for %d elements successfully.\n", n);

    // TODO: Step 5 - Free the dynamically allocated memory using free and set it to NULL
    
    if(ptr == NULL){
        printf("Memory freed successfully.\n");
    }

    return 0;


}