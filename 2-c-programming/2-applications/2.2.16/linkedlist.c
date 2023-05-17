#ifdef __unix__

#include <stdlib.h>
#include <stdio.h>

#elif defined(_WIN32) || defined(WIN32)

#include <windows.h>
#include <stdio.h>

#endif

/*
 * compile this program using the following command:
 * 	gcc -Wall -g linkedlist.c -o linkedlist
 *
 * run this program using the following command:
 * 	valgrind ./linkedlist
 */

// TODO: create a struct called node that contains:
// 	1. an integer called data
// 	2. a pointer to the next node in the linked list


// TODO: declare node called head that contains the first element in the linked list

void addElement(int data);
void printList();
void cleanupList();

int main() {
	addElement(10);
	printList();
	addElement(20);
	addElement(45);
	addElement(34);
	printList();
	cleanupList();
}

/*
 * Adds node to linked list
 * Params:
 * 	int x - data to be added
 * Return: none
 */
void addElement(int x) {
	// TODO: create node using node struct and x

	// TODO: add node to linked list

}

/*
 * Prints elements in linked list
 * Params: none
 * Return: none
 */
void printList() {
	// TODO: iterate through linked list

	// TODO: print index in linked list and data for all elements in linked list

}

/*
 * Frees dynamically allocated memory in linked list
 * Params: none
 * Return: none
 */
void cleanupList() {
	// TODO: free any dynamically allocated memory in your list

}
