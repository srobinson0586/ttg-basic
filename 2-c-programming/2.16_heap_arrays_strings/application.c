#include <stdio.h>
#include <stdlib.h>


int* heapArray = NULL;

void printArray(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// TODO: allocate and assign values for heapArray given the size of the array.   
// TODO: Check if memory allocation was successful
// TODO: itterate through the array and assign the value 0-size to the elements in the array.
void allocateArray(int size){


    
}

int main() {
    // TODO: Explain what the heap is and why it's useful
    printf("Heap and Arrays in C\n");

    // TODO: Explain dynamic memory allocation and the use of malloc
    int size;
    printf("Enter the size of the array: ");
    scanf("%d", &size);

    if (size <= 0) {
        printf("Invalid size!\n");
        return 1;
    }

    // TODO: implement allocateArray()
    allocateArray(size);

    // TODO: free heapArray
    

    return 0;
}