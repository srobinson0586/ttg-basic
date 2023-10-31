#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _node{
	int value;
	struct _node *parent;
	struct _node *left;
	struct _node *right;
}node;

typedef struct _binary_search_tree{
	node* root;
} BST;

/*
*	Creates a node with the specified value
*	Its parent, left, and right pointers are set to NULL
*	param:
*		int value - the value of the node
*	returns:
*		node* - a pointer to the newly allocated node
*/
node* create_node(int value);

/*
*  	Creates a BST with num_nodes nodes and returns the new root
*   Each node will have random values, and BST structure will be maintained
* 	params: 
*			int num_nodes - number of nodes to populate the tree with
*	returns:
*			node* - the root of the new tree
*/
BST* create_BST(int num_nodes);

/*
*  	Finds a node within the BST with the given value using Depth-First-Search (DFS)
* 	params: 
*			BST* bst - pointer to the BST in which to search
*			int value - number value of the node to return
*	returns:
*			node* - the node you are looking for or NULL if node not found
*/
node* find_node(BST* bst, int value);

/*
*  	Removes the node with the given value from the BST, however it does not free it
*   The caller is responsible for freeing it after done using it
*	Utilizes find_node()
* 	params: 
*			BST* bst - pointer to the BST from which to remove a node from
*			int value -   the value of the node to remove
*	returns:
*			node* - the node you are removing or NULL if node not found
*/
node* remove_node(BST* bst, int value);

/*
*  	Places a node within the BST based on its value, maintaining BST structure
* 	params: 
*			BST* bst - pointer to the BST in which to add a node
*			node* n  - the node to add into the binary search tree
*	returns:
*			void
*/
void add_node(BST* bst, node* n);

/*
*  	Prints the BST from the node with the smallest value to the one with the largest (DFS)
* 	params: 
*			BST* bst - pointer to the BST to print
*	returns:
*			void
*/
void print_tree(BST* bst);

/*
*  	Removes and frees all nodes from the bst in DFS
* 	params: 
*			BST* bst - pointer to the BST to destroy
*	returns:
*			void
*/
void destroy_tree(BST* bst);
