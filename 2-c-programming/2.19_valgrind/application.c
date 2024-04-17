#include <stdio.h>
#include <stdlib.h>

// Define a node structure for the linked list
struct Node {
    int data;
    struct Node *next;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        return NULL;
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to insert a node at the beginning of the linked list
void insertAtEnd(struct Node **head, int data) {
    struct Node* newNode = createNode(data);
    struct Node* temp = *head;
    if(temp == NULL){
        *head = newNode;
        return;
    }
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}

// Function to print the elements of the linked list
void printList(struct Node *head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

// Function to delete the entire linked list
void deleteList(struct Node **head) {
    struct Node* current = *head;
    struct Node* temp;
    while(current->next != NULL){
        temp=current->next;
        free(current);
        current=temp;
    
    }
    *head = NULL;
}

int main() {
    // Create an empty linked list
    struct Node* head = NULL;

    // Insert some elements into the linked list
    insertAtEnd(&head, 3);
    insertAtEnd(&head, 5);
    insertAtEnd(&head, 7);
    printList(head);
    // TODO: there is a memory leak in delete list. Modify the code to fix it. Use valgrind to check if memory leak are fixed.
    deleteList(&head);
    printList(head);
    return 0;
}