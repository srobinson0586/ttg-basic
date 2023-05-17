#ifdef __unix__

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#elif defined(_WIN32) || defined(WIN32)

#include <windows.h>
#include <stdio.h>

#endif

#include "structs.h"

/*
 * Compile proram like:
 *      $ gcc -g structs.c -o structs
 * 
 * Run program like:
 *      $ valgrind ./structs
 */

void createLibrary(BOOK *library);
void printLibrary(BOOK* library, int num_books);

int main() {
    int num_books = 3;
    // TODO: dynamically allocate a buffer to hold 3 books
    
    // TODO: implement and call createLibrary
    // TODO: implement and call printLibrary
    // TODO: cleanup
}

/*
 * Create 3 books with the following specifications
 * Params:
 *      BOOK* library - ptr to BOOK structs to populate
 * Return:
 *      none
 */
void createLibrary(BOOK* library) {
    // first book
    // title: Hamlet
    // author: William Shakespeare
    // call number: 822
    // category: drama

    // second book
    // title: Brave New World
    // author: Aldous Huxley
    // call number: 823
    // category: fiction

    // third book
    // title: The Art of War
    // author: Sun Tzu
    // call number: 355
    // category: Military science
}

/*
 * Print information about each book
 *      int num_books - number of BOOK structs to print
 * Return:
 *      none
 */
void printLibrary(BOOK* library, int num_books) {
    // TODO: print the following information for each BOOK struct
    // Index within the library
    // Book title
    // Book author

}
