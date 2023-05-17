#include <stdlib.h>
#include <stdio.h>
#include <string.h>


typedef struct _node{
	int id;
	struct _node *next;
} node;

void add_node(node** list, int id);
void delete_node(node** list, node* del);
void remove_node(node** list, int id);
node* create_list(int num_nodes);
node* find_node(node* list, int id);
void swap_nodes(node** list, node* i, node* j);
void sort_list(node** list);
void insert_node(node** list, node* n, int location);
void destroy_list(node* list);
void print_list(node* list);