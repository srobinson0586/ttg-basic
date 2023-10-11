#include "doubly_linked_list.h"

/*
*	Use main to create a testing suite to test your implementation
*/
int main(int argc, char** argv){
	node* list = NULL;
	return 0;
}	

/*
*  	Allocates a node with the given id to place at the end of the list
* 	params: 
*			node** list - address of the head of your doubly linked list
*			int id      - number id to place into the node
*	returns:
*			void
*/
void add_node(node** list, int id){
}

/*
* 	Removes the node from your doubly linked list
* 	params:
*			node** list - address of the head of your doubly linked list
*			node* del 	- the node you want to remove from the doubly linked list
*	returns:
*			none - doesn't return anything but passed node is taken out of list
*
*/
void delete_node(node** list, node* del){
	return;
}

/*
* 	Removes first instance of a node from the list given the id
* 	params:
*			node** list - address of the head of your doubly linked list
*			int id 		- number id to search for removal
*	returns:
*			none - doesn't return anything but first node with given information is taken out of list
*/
void remove_node(node** list, int id){
	return;
}

/*
* 	Creates a doubly linked list with given number of nodes.
* 	params:
*			int num_nodes - number of nodes to create
*	returns:
*			node* - returns the head of the created list
*/
node* create_list(int length){
	return NULL;
}

/*
* 	Returns first instance of a node from the list given the id
* 	params:
*			node* list 	- address of the head of your doubly linked list
*			int id 		- number id to place into the node
*	returns:
*			node* - returns a pointer to the node with the given information
*/
node* find_node(node* list, int id){
	return NULL;
}

/*
* 	Given the list and two nodes it swaps the order of those two nodes
* 	params:
*			node** list - address of the head of your doubly linked list
*			node* i 	- first node to swap
*			node* j 	- second node to swap
*	returns:
*			none - doesn't return anything but the order of the two nodes will be swapped in the list
*/
void swap_nodes(node** list, node* i, node* j){
	return;
}

/*
* 	Sorts the doubly linked list in ascending order.
* 	params:
*			node** list - address of the head of the doubly linked list
*	returns:
*			none - the list will be sorted after the function executes
*
*/
void sort_list(node** list){
	return;
}

/*
* 	Inserts a given node into the list at the provided location (0 makes it the head of the list, 
*		anything greater than the length of the list puts it at the end.)
* 	params:
*			node** list 	- address of the head of the doubly linked list
*			node* n 		- the node to insert into the doubly linked list
*			int location 	- the location to add the node at
*	returns:
*			none - but the doubly linked list has changed to include the new node
*/
void insert_node(node** list, node* n, int location){
	return;
}

/*
* 	Completely destroys the doubly linked list
* 	params: 
*			node* list - pointer to head of the doubly linked list
*	returns: 
*			void - doesn't return anything but frees all allocated memory
*
*/
void destroy_list(node* list){
	return;
} 

/*
* 	Prints the entire doubly linked list in order
* 	params:
*			node* list - head of the doubly linked list to print
*	returns:
*			none - doesnt return anything but prints the nodes to STDOUT
*/
void print_list(node* list){
	return;
}

/*
*  	Calculates the length of the list
* 	params: 
*			node* list - the head of the list to get the length of
*	returns:
*			int - the number of nodes in the list
*/
int get_length(node* list){
	return -1;
}
