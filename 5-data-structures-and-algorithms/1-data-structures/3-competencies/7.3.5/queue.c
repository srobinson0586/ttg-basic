#include "queue.h"

/*
*	Use main to create a testing suite to test your implementation
*/
int main(int argc, char** argv){
	return 0;
}	

/*
* 	Adds node to end of queue
* 	params:
*			node** queue - the queue to be pushed to
*			int id 		 - id of the node to be added
*	returns:
*			none - doesn't return anything but node is appended to queue
*
*/
void enqueue(node** queue, int id){
	return;
}

/*
* 	Removes first node from queue
* 	params:
*			node** queue - the queue to be popped from
*	returns:
*			int - the id of the popped node
*
*/
int dequeue(node** queue){
	return -1;
}

/*
* 	Creates a queue with given number of nodes. Each node has a letter in them that is incremented.
* 	params:
*			int num_nodes - number of nodes to create
*	returns:
*			node* - A pointer to the head node of the queue
*/
node* create_queue(int num_nodes){
	return NULL;
}

/*
* 	Returns first instance of a node from the queue given the id
* 	params:
*			node** queue - the queue to be removed from 
*			int id 		 - id of node to find
*	returns:
*			node* - returns a pointer to the node with the given information
*/
node* find_node(node** queue, int id){
	return NULL;
}

/*
* 	Removes the node from your queue
* 	params:
*			node** queue - the queue to be removed from
*			int id       - id of the node to remove
*	returns:
*			none - doesn't return anything but node with id is taken out of queue
*
*/
void remove_node(node** queue, int id){
	return;
}

/*
* 	Completely destroys the queue
* 	params: 
*			node** queue - the queue to be destroyed
*	returns: 
*			void - doesn't return anything but frees all allocated memory
*
*/
void destroy_queue(node** queue){
	return;
}

/*
* 	Prints the entire queue in order
* 	params:
*			node** queue - the queue to be printed
*	returns:
*			none - doesnt return anything but prints the nodes to STDOUT
*/
void print_queue(node** queue){
	return;
}
