#include <stdlib.h>
#include <stdio.h>
#include <string.h>


typedef struct _node{
	int id;
	struct _node *next;
} node;

void enqueue(node** queue, int id);
int dequeue(node** queue);
node* create_queue(int num_nodes);
node* find_node(node** queue, int id);
void remove_node(node** queue, int id);
void destroy_queue(node** queue);
void print_queue(node** queue);
