#ifndef LINKED_LIST_H
#define LINKED_LIST_H

struct node {
    int data;
    struct node* next;
};

struct node* new_node(int data);

void add_node(struct node* head, struct node* node);

void free_list(struct node* head);

void print_list(struct node* head);

void patch_jmp_table(void* malloc, void* free, void* printf);

#endif
