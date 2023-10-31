#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _node{
    int data;
    struct _node* next;
} node;

typedef struct _stack{
    int size;   // total number of nodes
    node* top;  // the 'top' node
} Stack;

/*  Creates a node with the specified data.
*   It's next member is set to null
*   params:
*           int data - the value to hold within the stack node
*   returns:
*           node* - A pointer to the new node. NULL on failure.
*/
node* create_node(int data);

/*
*   Creates a stack of `size` nodes.
*   Each node has a random `data` member.
*   Utilizes the `push()` method
*   params:
*           node* first_node
*   returns:
*           Stack* - A pointer to the new stack
*/
Stack* create_stack_n(int size);

/*
*   Pushes a node to the top of the stack (FILO)
*   params:
*           Stack* stack - the stack to use
*           node* n  - the node to add
*   returns:
*           void
*/
void push(Stack* stack, node* n);

/*
*   Pops node off the top of the stack (FILO)
*   params:
*           Stack* stack - the stack to use
*   returns:
*           node* - the popped node or NULL if the stack is empty
*/
node* pop(Stack* stack);

/*
*   Removes n nodes from the stack. Utilizes the pop() method.
*   Ensures arguments are valid
*   params:
*           Stack* stack - the stack to use
*           int n        - the amount of elements to remove
*   returns:
*           int - The amount of elements removed (not necessarily `n` in case of failure)
*/
int rem_n_nodes(Stack* stack, int n);

/*
*   Removes and frees all nodes on `*stack`
*   Frees `*stack` as well and sets it to null
*   params:
*           Stack** stack - the stack to destroy
*   returns:
*           void
*/
void destroy_stack(Stack** stack);

/*
*   Prints all nodes on the stack, without popping them
*   For debugging purposes
*   params:
*           Stack* stack
*   returns:
*       void
*/
void print_stack(Stack* stack);
