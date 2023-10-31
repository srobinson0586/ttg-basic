#include <stdlib.h>
#include <stdio.h>
#include <string.h>


typedef struct _node{
	int priority;
	int data;
	struct _node *next;
} node;

typedef struct _priority_queue{
	int size;
	node* front; 
} PQ;

/*  Creates a node with the specified data and priority.
*   It's next member is set to null.
*   params:
*			int priority - the node's priority
*           int data - the value to hold within the stack node
*   returns:
*           node* - A pointer to the new node. NULL on failure.
*/
node* create_node(int data);

/*
* 	Creates a priority queue with given number of nodes
*   Each node has a random priority from 0 TO `num_nodes` (PQ size)
*	Node insertion is done with the `enqueue` method
*	As in conventional Operating System Kernel Priority Queues,
*		lesser `priority` values mean the node has *higher priority* in enqueue/dequeue operations
*		e.g. a node with priority==1 is more important than a node with priority==3
* 	params:
*			int num_nodes - number of nodes to create
*	returns:
*			PQ* - A pointer to the head node of the queue
*/
PQ* create_queue(int num_nodes);

/*
* 	Adds `node` to the queue depending on its priority.
*	If a node with that priority already exists, its inserted before the existing node.
*	Ripple effects must be accounted for, i.e. updating the rest of the nodes
*	e.g
*	  PQ my_queue = { (node1; priority=1) --> (node2; priority=2) --> (node3; priority=3) };
*	  enqueue( my_queue, (node4; priority=2) );
*	  my_queue == {
	    (node1; priority=1) --> (node4; priority=2) --> (node2; priority=3) --> (node3; priority=4)
	  }
* 	params:
*			PQ* queue - the queue to be pushed to
*			node* node - the node to be added
*	returns:
*			none - doesn't return anything but node is inserted into the queue
*/
void enqueue(PQ* queue, node* node);

/*
* 	Removes the highest priority node from `queue`
*	However, it does not free it, so that the caller may use the pointer
*	The caller is responsible for freeing it once finished with the data
* 	params:
*			PQ* queue - the queue to be popped from
*	returns:
*			node* - a pointer to the popped node
*/
node* dequeue(PQ* queue);

/*
* 	Completely destroys the queue, freeing everything, including `*queue`
*	Sets `*queue` to NULL
* 	params: 
*			PQ** queue - the queue to be destroyed
*	returns: 
*			void - doesn't return anything but frees all allocated memory
*/
void destroy_queue(PQ** queue);

/*
* 	Prints the entire queue in order of node priority
* 	params:
*			PQ* queue - the queue to be printed
*	returns:
*			none - doesn't return anything but prints the nodes to STDOUT
*/
void print_queue(PQ* queue);
