#include <stdio.h>
#include <stdlib.h>


int* heapArray = NULL;

void printArray(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// TODO: Allocate and assign values for heapArray given the size of the array.   
// TODO: Check if memory allocation was successful.
// TODO: Iterate through the array and assign the values 0, 1, 2, ... to the elements in the array.
void allocateArray(int size){


    
}

int main() {

    printf("Heap and Arrays in C\n");

    int size;
    printf("Enter the size of the array: ");
    scanf("%d", &size);

    if (size <= 0) {
        printf("Invalid size!\n");
        return 1;
    }

    // TODO: implement allocateArray()
    allocateArray(size);

    printArray(heapArray, size);

    // TODO: free heapArray
    

    return 0;
}