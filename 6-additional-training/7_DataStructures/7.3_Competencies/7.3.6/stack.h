#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct _node{
    int id;
    struct _node* next;
} node;

void push_node(node** stack, node* n);
node* get_nth_node(node** stack, int n);
node* pop_node(node** stack);
node* create_stack_n(int n);
void rem_nth_node(node** stack, int n);
void print_stack(node** stack);
void destroy_stack(node** stack);