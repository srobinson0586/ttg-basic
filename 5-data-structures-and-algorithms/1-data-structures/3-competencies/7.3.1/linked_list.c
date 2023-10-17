#include "linked_list.h"

/*
*	Use main to create a testing suite to test your implementation
*/
int main(int argc, char** argv) {
	node* list = NULL;
	return 0;
}	

/*
*  	Allocates a node with the given id to place at the end of the list
* 	params: 
*			node** list - address of the head of your linked list
*			int id - number id to place into the node
*	returns:
*			void
*/
void add_node(node** list, int id){
	return;
}

/*
* 	Removes the node from your linked list
* 	params:
*			node** list - address of the head of your linked list
*			node* del 	- the node you want to remove from the linked list
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
*			node** list - address of the head of your linked list
*			int id 		- number id to search for removal
*	returns:
*			none - doesn't return anything but first node with given information is taken out of list
*/
void remove_node(node** list, int id){
	return;	
}

/*
* 	Creates a list with given number of nodes.
* 	params:
*			int num_nodes - number of nodes to create
*	returns:
*			node* - returns the head of the created list
*/
node* create_list(int num_nodes){
	return NULL;
}

/*
* 	Returns first instance of a node from the list given the id
* 	params:
*			node* list 	- address of the head of your linked list
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
*			node** list - address of the head of your linked list
*			node* i 	- first node to swap
*			node* j 	- second node to swap
*	returns:
*			none - doesn't return anything but the order of the two nodes will be swapped in the list
*/
void swap_nodes(node** list, node* i, node* j){
	return;
}

/*
* 	Sorts the linked list in ascending order.
* 	params:
*			node** list - address of the head of the linked list
*	returns:
*			none - The list will be sorted after the function executes
*
*/
void sort_list(node** list){
	return;
}

/*
* 	Inserts a given node into the list at the provided location (0 makes it the head of the list, 
*		anything greater than the length of the list puts it at the end.)
* 	params:
*			node** list 	- address of the head of the linked list
*			node* n 		- the node to insert into the linked list
*			int location 	- the location to add the node at
*	returns:
*			none - but the linked list has changed to include the new node
*/
void insert_node(node** list, node* n, int location){
	return;
}

/*
* 	Completely destroys the linked list
* 	params: 
*			node* list - pointer to head of the linked list
*	returns: 
*			void - doesn't return anything but frees all allocated memory
*
*/
void destroy_list(node* list){
	return;
}

/*
* 	Prints the entire linked list in order
* 	params:
*			node* list - head of the linked list to print
*	returns:
*			none - doesnt return anything but prints the nodes to STDOUT
*/
void print_list(node* list){
	return;
}
