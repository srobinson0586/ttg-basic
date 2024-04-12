# C Programming - Linked Lists

## Overview
A linked list is a fundamental data structure used in computer science to organize and store data. It consists of a sequence of elements called nodes, where each node contains two parts: the data and a reference (pointer) to the next node in the sequence. The last node typically points to a null reference, indicating the end of the list.

### As Compared to Arrays
Arrays and linked lists are both data structures used to store collections of elements, but they differ in several key aspects: 

| Feature                           | Arrays                                       | Linked Lists                                 |
|-----------------------------------|----------------------------------------------|----------------------------------------------|
| Memory Allocation                 | Fixed size, pre-allocated memory             | Dynamic size, memory allocated as needed     |
| Access Time                       | Constant time for direct access by index     | Requires traversal for access               |
| Insertions/Deletions              | Inefficient, may require shifting elements | Efficient, updating pointers is sufficient |
| Memory Efficiency                 | May have wasted memory due to pre-allocation| More memory-efficient for dynamic sizing    |
| Size Flexibility                  | Fixed size, difficult to resize dynamically | Dynamic size, easily resizable               |
| Implementation of Other Data Structures | Building blocks for various data structures | Fundamental for implementing complex data structures |
| Ease of Use                       | Simpler syntax for direct access and iteration | Requires traversal, slightly more complex   |

### Code Example

In this example, the array is statically initialized with values, and the linked list is dynamically created by inserting nodes at the beginning. The code then prints the contents of both the array and the linked list. Finally, it frees the memory used by the linked list.

```c
#include <stdio.h>
#include <stdlib.h>

// Node structure for linked list
struct Node {
    int data;
    struct Node* next;
};

int main() {
    // Example with an array
    int array[5] = {10, 20, 30, 40, 50};

    printf("Array: ");
    for (int i = 0; i < 5; ++i) {
        printf("%d ", array[i]);
    }
    printf("\n");

    // Example with a linked list
    struct Node* head = NULL;

    // Insert at the beginning
    for (int i = 5; i > 0; --i) {
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = i * 10;
        newNode->next = head;
        head = newNode;
    }

    printf("Linked List: ");
    struct Node* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");

    // Free the memory used by the linked list
    current = head;
    while (current != NULL) {
        struct Node* next = current->next;
        free(current);
        current = next;
    }

    return 0;
}
```

### Key Characteristics

1. **Dynamic Size:**
   - Linked lists can dynamically grow or shrink in size during program execution. Unlike arrays, which have a fixed size, linked lists allow you to add or remove elements easily without the need to pre-allocate a specific amount of memory.

2. **Efficient Insertions and Deletions:**
   - Insertions and deletions in a linked list are more efficient compared to arrays. In an array, if you want to insert or delete an element, you might need to shift all subsequent elements, which can be time-consuming. In a linked list, you can easily update pointers to insert or delete elements without the need for such shifts.

3. **No Pre-allocation of Memory:**
   - Linked lists do not require pre-allocation of memory for a fixed number of elements. Memory is allocated dynamically as nodes are added, making linked lists suitable for situations where the size of the data is unknown or can change over time.

4. **Easy Implementation of Data Structures:**
   - Linked lists are used as building blocks for implementing other data structures such as stacks, queues, and symbolic expressions. Their simplicity and flexibility make them a fundamental part of more complex data structures.

5. **No Wasted Memory:**
   - Unlike arrays, which may allocate more memory than necessary due to a predefined size, linked lists allocate memory only for the elements they contain. This can reduce memory waste in situations where the actual size of the data is smaller than the allocated space in an array.

6. **Memory Efficiency for Random Insertions:**
   - If you need to frequently insert elements in the middle of a data structure, linked lists are more memory-efficient than arrays. In arrays, you might need to shift a significant portion of the elements, while in linked lists, you just need to update pointers.

However, linked lists also have some disadvantages, such as the lack of direct access to elements by index, and they may use more memory than arrays due to the overhead of storing pointers. The choice between linked lists and other data structures depends on the specific requirements and constraints of your application.

### Linked List Structure:

A linked list is made up of nodes. Each node has two parts:
1. **Data part:** Contains the actual data you want to store.
2. **Next part (Pointer):** Points to the next node in the sequence.

The last node typically has a NULL (or equivalent) pointer as there is no next node.

### Basic Operations:
1. **Insertion:**
    - **At the beginning:**
        - Create a new node.
        - Make the new node point to the current head.
        - Update the head to the new node.

    - **At the end:**
        - Create a new node.
        - Traverse the list to the last node and make it point to the new node.
        - Update the new node's pointer to NULL.

2. **Deletion:**
    - **At the beginning:**
        - Update the head to the next node.
        - Free the memory of the deleted node.

    - **At the end:**
        - Traverse the list until the second-to-last node.
        - Update its pointer to NULL.
        - Free the memory of the deleted node.

3. **Traversal:**
    - Use a loop to go through each node in the list.

### Implementation

This example program creates a linked list, inserts elements at the beginning and end, deletes elements at the beginning and end, and finally prints the list.

```c
#include <stdio.h>
#include <stdlib.h>

// Node structure
struct Node {
    int data;
    struct Node* next;
};

// Function to insert a new node at the beginning of the list
void insertAtBeginning(struct Node** head, int newData) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = newData;
    newNode->next = *head;
    *head = newNode;
}

// Function to insert a new node at the end of the list
void insertAtEnd(struct Node** head, int newData) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    struct Node* last = *head;

    newNode->data = newData;
    newNode->next = NULL;

    if (*head == NULL) {
        *head = newNode;
        return;
    }

    while (last->next != NULL)
        last = last->next;

    last->next = newNode;
}

// Function to delete a node at the beginning of the list
void deleteAtBeginning(struct Node** head) {
    if (*head == NULL)
        return;

    struct Node* temp = *head;
    *head = temp->next;
    free(temp);
}

// Function to delete a node at the end of the list
void deleteAtEnd(struct Node** head) {
    if (*head == NULL)
        return;

    struct Node* temp = *head;
    struct Node* prev = NULL;

    while (temp->next != NULL) {
        prev = temp;
        temp = temp->next;
    }

    if (prev != NULL)
        prev->next = NULL;

    free(temp);
}

// Function to print all nodes in the list
void printList(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

// Function to free all nodes in the list
void freeList(struct Node** head) {
    struct Node* current = *head;
    struct Node* next;

    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }

    *head = NULL;
}

// Example usage
int main() {
    struct Node* head = NULL;

    insertAtEnd(&head, 10);
    insertAtBeginning(&head, 5);
    insertAtEnd(&head, 20);
    insertAtBeginning(&head, 2);

    printf("Linked list: ");
    printList(head);

    deleteAtEnd(&head);
    deleteAtBeginning(&head);

    printf("Linked list after deletion: ");
    printList(head);

    freeList(&head);

    return 0;
}
```