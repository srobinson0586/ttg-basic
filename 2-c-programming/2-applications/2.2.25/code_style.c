#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

/*
    ##### Code Snippets ######

    Here are 6 examples. For each example, do the following:
    1) Write a brief comment on how the example violates C style, and
    2) Write a correct version underneath (copy and paste new code with changes)

    NOTE: Ignore generic variable names unless otherwise instructed.
*/

/* ============ Example 1 ============ */
size_t i=0;
for(i=0;i<10;i++){
    doStuff();
}
/*
    1) How does this violate C style?
        ANSWER: TODO:
    2) Copy and paste example below, then correct code.
*/
// TODO: Code goes here


/* ============ Example 2 ============ */
int32_t a = sum (4, 3);
/*
    1) How does this violate C style?
        ANSWER: TODO:
    2) Copy and paste example below, then correct code.
*/
// TODO: Code goes here


/* ============ Example 3 ============ */
my_func(size_t size) {
    int32_t* arr;
    arr = malloc(sizeof *arr * size);  
    if (arr == NULL) {
        exit(EXIT_FAILURE); // FAIL, no memory
    }

    free(arr);  // Free memory after usage
}
/*
    1) How does this violate C style?
        ANSWER: TODO:
    2) Copy and paste example below, then correct code.
*/
// TODO: Code goes here


/* ============ Example 4 ============ */
void boo() {
    int32_t a;
    a = bar();
    int32_t b;
    b = foo(); 
}     
/*
    1) How does this violate C style?
        ANSWER: TODO:
    2) Copy and paste example below, then correct code.
*/
// TODO: Code goes here


/* ============ Example 5 ============ */
if (c)
    do_a();
else
    do_b();   
/*
    1) How does this violate C style?
        ANSWER: TODO:
    2) Copy and paste example below, then correct code.
*/
// TODO: Code goes here


/* ============ Example 6 ============ */
int building_volume(int e, int f, int g) {
    int d = e * f * g;
    return (d);
}  
/*
    1) How does this violate C style? Consider variable naming for this one.
        ANSWER: TODO:
    2) Copy and paste example below, then correct code.
*/
// TODO: Code goes here


/* =================================== */
