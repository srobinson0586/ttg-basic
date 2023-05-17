#include <stdio.h>
#include <stdlib.h>
#include <strings.h>


typedef struct _node{
	int id;
	struct _node *left;
	struct _node *right;
}node;

node* find_node(node* root, int id);
node* min_val_node(node* root);
node* remove_node(node* root, int id);
int num_children(node* root);
void place_node(node** root, node* n);
node* create_tree(int num_nodes);
void print_tree(node* root);
void free_tree(node* root);
