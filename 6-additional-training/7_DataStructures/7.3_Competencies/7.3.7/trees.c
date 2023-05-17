#include "trees.h"

/*
*	Use main to create a testing suite to test your implementation
*/
int main(){
	return 0;
}

/*
*  	Finds a node within the tree
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
*  	Finds smallest node in the tree from the given root
* 	params: 
*			node* root - pointer to the root node of the tree
*	returns:
*			node* - the smallest node in the tree
*/
node* min_val_node(node* root){
	return NULL;
}

/*
*  	Removes the node with the given id from the tree
* 	params: 
*			node* root - pointer to the root node of the tree
*			int id - number id of the node to remove
*	returns:
*			node* - the node you are trying to remove or NULL if node not found
*/
node* remove_node(node* root, int id){
	return NULL;

}

/*
*  	Returns number of children a node has
* 	params: 
*			node* root - pointer to the root node of the tree
*	returns:
*			int - number of direct children off of given node
*/
int num_children(node* root){
	return -1;
}

/*
*  	Places a node within a tree
* 	params: 
*			node** root - address of the pointer to the root node of the tree
*			node*  n 	- the node to add into the tree
*	returns:
*			void
*/
void place_node(node** root, node* n){
	return;
}

/*
*  	Create a tree with num_nodes number of nodes in it
* 	params: 
*			int num_nodes - number of nodes to add to the created tree
*	returns:
*			node* - the root node of the created tree
*/
node* create_tree(int num_nodes){
	return NULL;
}

/*
*  	Prints the tree with inorder traversal
* 	params: 
*			node* root - pointer to the root node of the tree
*	returns:
*			void
*/
void print_tree(node* root){
	return;
}

/*
*  	Removes and frees the tree
* 	params: 
*			node* root - pointer to the root node of the tree
*	returns:
*			void
*/
void free_tree(node* root){
	return;
}