#include "hash_table.h"

/*
*	Use main to create a testing suite to test your implementation
*/
int main(){
	return 0;
}

/*
*  	Creates hash table with n elements
* 	params: 
*			int n  - number of elements to add to hash table
*	returns:
*			node** - the newly created hash table
*/
node** create_table(int n){
	return NULL;
}

/*
*  	Finds the data in the hash table and returns that element
* 	params: 
*			node** table - the hash table to search
*			int data 	 - data to search for in hash table
*			int n 	 	 - number of buckets in hash table
*	returns:
*			node* 	 	 - the node you are searching for or NULL if it doesn't exist
*/
node* find_node(node** table, int data, int n){
	return NULL;
}

/*
*  	Removes the node with the corresponding data from the hash table
* 	params: 
*			node** table - the hash table to use
*			int data 	 - the data value to look for to remove the node
*			int n 	 	 - the number of buckets in the hash table
*	returns:
*			void
*/
void remove_node(node** table, int data, int n){
	return;
}

/*
*  	Adds the provided node into the hash table
* 	params: 
*			node** table - the hash table to use
*			node* obj 	 - the node to add into the hash table
*			int n 	  	 - the number of buckets in the hash table
*	returns:
*			void
*/
void add_node(node** table, node* obj, int n){
	return;
}

/*
*  	Prints the entire hash table in order of bucket and all nodes in that bucket before moving on
* 	params: 
*			node** table - the hash table to use
*			int n 	 	 - the number of buckets in the hash table
*	returns:
*			void
*/
void print_table(node** table, int n){
	return;
}

/*
*  	Removes and frees the entire hash table
* 	params: 
*			node** table - the hash table to destroy
*			int n 	     - the number of buckets in the hash table
*	returns:
*			void
*/
void destroy_table(node** table, int n){
	return;
}