#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define TABLE_SIZE 10

typedef struct _hash_node{
	int id;
	struct _hash_node *next;
}node;


node** create_table(int n);
node* find_node(node** table, int data, int n);
void remove_node(node** table, int data, int n);
void add_node(node** table, node* obj, int n);
void print_table(node** table, int n);
void destroy_table(node** table, int n);
