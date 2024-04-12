#include <stdio.h>
#include <stdlib.h>

// Define a structure for each node in the linked list
struct Node {
    int data;
    struct Node* next;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to insert a new node at the beginning of the linked list
void insertAtBeginning(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}

// TODO: Implement this function that traverses through a linked list and prints all the values.
void printLinkedList(struct Node* head) {
  
}
//TODO: Implement this function that frees every value and sets the head to NULL
void clearLinkList(head){

}
int main() {
    struct Node* head = NULL; // Initialize an empty linked list


    insertAtBeginning(&head, 5);
    insertAtBeginning(&head, 10);
    insertAtBeginning(&head, 15);

    printLinkedList(head);

    insertAtBeginning(&head, 20);
    insertAtBeginning(&head, 25);
    
    printLinkedList(head);

    clearLinkList(head);
    
    printLinkedList(head);

    return 0;
}