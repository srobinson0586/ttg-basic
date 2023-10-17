#include "binary_search_tree.h"

/*
*	Use main to create a testing suite to test your implementation
*/
int main(){
	return 0;
}

/*
*  	Finds a node within the binary search tree
* 	params: 
*			node* root - pointer to the root node of the tree
*			int id - number id of the node to return
*	returns:
*			node* - the node you are looking for or NULL if node not found
*/
node* find_node(node* root, int id){
	return NULL;
}

/*
*  	Finds the smallest node within the binary search tree (relative to passed node)
* 	params: 
*			node* root - pointer to the root node of the tree
*	returns:
*			node* - the furthest left node
*/
node* min_val_node(node* root){
	return NULL;
}

/*
*  	Removes the node with the given id from the binary search tree
* 	params: 
*			node* root - pointer to the root node of the tree
*			int id - number id of the node to remove
*	returns:
*			node* - the node you are removing or NULL if node not found
*/
node* remove_node(node* root, int id){
	return NULL;
}

/*
*  	Places a node within the binary search tree
* 	params: 
*			node*  n 	- the node to add into the binary search tree
*			node** root - address of the pointer to the root node of the tree
*	returns:
*			node* - the node you are looking for or NULL if node not found
*/
void place_node(node* n, node** root){
	return;
}

/*
*  	Creates a binary search tree with num_nodes nodes and returns the new root
* 	params: 
*			int num_nodes - number of nodes to populate the tree with
*	returns:
*			node* - the root of the new tree
*/
node* create_binary_search_tree(int num_nodes){
	return NULL;
}

/*
*  	Prints the tree from smallest to largest node
* 	params: 
*			node* root - pointer to the root node of the tree
*	returns:
*			void
*/
void print_tree(node* root){
	return;
}

/*
*  	Destroys and frees allocated memory of the tree.
* 	params: 
*			node* root - pointer to the root node of the tree
*	returns:
*			void
*/
void free_tree(node* root){
	return;
}
