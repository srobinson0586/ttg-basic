#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// allow for stored data type configuration at runtime
#define HT_DATA char*
/* 
* Our hash table structure. It's size will be determined dynamically at initialization.
* It will contain an array of  C-String values that can be accessed using a string key
* The hash() function will be used to determine the index in the array that contains
*	a key's value.
* Example:
* hash_table{
	buckets = 3
	dataArray{
		"p@ssw0rd",
		"Il0veY0u",
		"qwerty"
	}
  }

  char* bobPassword = hash_table->data[ hash("bob") ];
*/
typedef struct _hash_table{
	int buckets;		// Amount of elements (size)
	HT_DATA* dataArray; // Array of pointers to the data
} hash_table;

/*
*  	Creates a hash table with size of `size`
*   Initializes all `dataArray` elements to NULL.
* 	params: 
*			int size  - number of elements to add to hash table
*	returns:
*			hash_table* - the newly created hash table
*				or NULL on failure
*/
hash_table* create_table(int size);

/* 
*	Takes a string key and returns a pointer to it's address in the `table.dataArray` member
*   i.e. if dataArray is at 0x30000000 and the key's calculated index is 1, this returns 0x30000008
*
*	Must minimize collisions. Can't return indexes out of range.
*	Should be used *every time insertion/deletion/reading of a single element is being done on the HT*
*	params:
*			hash_table* - The table you want to search
*			char* key - The key to calculate the desired data's index from
*	returns:
*			HT_DATA - The address for the corresponding value's pointer or NULL on failure.
*/
HT_DATA hash(hash_table* table, char* key);

/*
*  	Removes the data at the corresponding index in the `table.dataArray` member
*	By 'Remove', we mean free() the pointer at that index and set that index to NULL.
* 	params: 
*			hash_table* table - the hash table to use
*			char*  key   - the key to hash and find an index with
*	returns:
*			void
*/
void remove_data(hash_table* table, char* key);

/*
*  	Adds the provided data into the hash table.
*	Must account for collisions on its call to hash() when determining the index to insert at
*	Since hash_table.dataArray elements that are considered empty when set to NULL,
*		this means a collision happens when hash() returns an index where it's element != NULL.
*	In that case, this function fails, doesn't attempt insertion, and notifies the caller.
* 	params: 
*			hash_table* table - the hash table to use
*			HT_DATA* value 	 - the value to add into the hash table
*	returns:
*			HT_DATA* - The address of the newly inserted node
*						or NULL on failure / collision
*/
void add_data(hash_table* table, HT_DATA* value);

/*
*  	Prints the entire hash table in order
* 	params: 
*			hash_table* table - the hash table to use
*	returns:
*			void
*/
void print_table(hash_table* table);

/*
*  	Frees the `table.dataArray` member and sets `table` to null
* 	params: 
*			hash_table** table - the hash table to destroy
*	returns:
*			void
*/
void destroy_table(hash_table** table);
