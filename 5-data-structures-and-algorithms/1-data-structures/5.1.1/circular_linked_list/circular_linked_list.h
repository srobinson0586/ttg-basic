#include <stdlib.h>
#include <stdio.h>
#include <string.h>


typedef struct _node{
	int id;			// a random value between 1 and 50
	struct _node *next;
} node;

typedef struct _circular_linked_list{
	node* head;
} CLL;

/*
* 	Creates a list with the given number of nodes.
*   Every new node's `id` should be a random value between 1 and 50.
*   The `id` member's value should be *unique* in the list
*   This function should use the add_node() function
* 	params:
*			int num_nodes - number of nodes to create
*	returns:
*			CLL* - returns the head of the created list
*					or NULL on failure
*/
CLL* create_list(int num_nodes);

/*
*  	Allocates a node with the given id to place at the end of the list.
* 	params: 
*			CLL* list - pointer to the CLL in which to add a node
*			int id - number id to place into the node
*	returns:
*			1 on failure, 0 on success
*/
int add_node(CLL* list, int id);

/*
* 	Returns a pointer to the first occurrence of a node from the list with the given id
* 	params:
*			CLL* list 	- pointer to the CLL in which to search for a node
*			int id 		- number id to place into the node
*	returns:
*			node* - returns a pointer to the node with the given id
*					or NULL on failure
*/
node* find_node(CLL* list, int id);

/* 
* 	Removes the first instance of a node from the list with the given the id
* 	params:
*			CLL* list - pointer to the CLL from which to remove a node
*			int id 		- number id to search for removal
*	returns:
*			1 on failure, 0 on success
*/
int remove_node(CLL* list, int id);

/*
* 	Inserts a given node into the list at the provided location 
*   	0 makes it the head of the list
*		anything greater than the length of the list puts it at the end
* 	params:
*			CLL* list 	- pointer to the CLL in which to insert
*			node* n 		- the node to insert into the CLL
*			int location 	- the location to add the node at
*	returns:
*			1 on failure, 0 on success
*/
int insert_node(CLL* list, node* n, int location);

/*
* 	Given the list and the id of two nodes it swaps the order of those two nodes.
*   i.e. Node A will be in the position Node B was in the CLL, and vice versa.
* 	params:
*			CLL* list - pointer to the CLL in which to swap nodes
*			int id_A 	- first node to swap
*			int id_B 	- second node to swap
*	returns:
*			1 on failure, 0 on success
*/
int swap_nodes(CLL* list, int id_A, int id_B);

/*
* 	Sorts the CLL in ascending order.
*	i.e. Nodes with lesser value ids will be closer to the Head of the CLL
* 	params:
*			CLL* list - pointer to the CLL which to sort
*	returns:
*			1 on failure, 0 on success
*/
int sort_list(CLL* list);

/*
* 	Completely destroys the CLL, i.e. free all nodes
* 	params: 
*			CLL* list - pointer to the CLL to destroy
*	returns: 
*			1 on failure, 0 on success
*/
int destroy_list(CLL* list);

/*
* 	Prints the entire CLL in order
* 	params:
*			CLL* list - head of the CLL to print
*	returns:
*			1 on failure, 0 on success
*/
int print_list(CLL* list);
