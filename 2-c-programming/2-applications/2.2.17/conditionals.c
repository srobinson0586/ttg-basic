#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>


// Instructions:
// Take your code from mutex.c and incorporate conditional variables to increment and 
// decrement 'counter'. For now, decrement when 'counter' > 14
// Here, you will need to make use of condition variables in order to send signal and wait objects

// play around with the wait and signal objects, what if you waited on dec_func and signaled on 
// inc_func, vise versa

// References:
// The reference below may help you in creating conditional variables: 
// https://www.youtube.com/watch?v=0sVGnxg6Z3k


#define NUM_THREADS 100
#define NUM_ITERS   10000000

// What will this be initialized to?
int counter;

// TODO: For thread safety, create a mutex variable to protect the counter (pthread_mutex_t)
// TODO: For condition safety, create a conditional variable (pthread_cond_t)


// Increment `counter` NUM_ITERS times.
void* inc_func(void* param) {
    // This will prevent gcc from complaining that `param` is an unused arg.
    (void) param;

    // TODO: Increment `counter` NUM_ITERS times, using a for loop.

    // TODO: set mutex lock
    // TODO: set signal object
    return NULL; // TODO: Change if needed
}

// Decrement `counter` NUM_ITERS times.
void* dec_func(void* param) {
    // This will prevent gcc from complaining that `param` is an unused arg.
    (void) param;

    // TODO: Decrement `counter` NUM_ITERS times, using a for loop.

    // TODO: set mutex lock
    
    // TODO: set your wait object
    return NULL; // TODO: Change if needed
}

int main() {
    pthread_t thread_array[NUM_THREADS] = {0};
    int create_rtn;
    int thread_idx;

    // TODO: For thread safety, initialize the counter mutex.
    // TODO: initialize your conditional variable


    // TODO: Create NUM_THREADS thread, and store their tids in thread_array.
    // TODO: Use pthread_join to wait for all threads to complete.
    // Print out information about the number of race errors.
    printf("counter = %d\n", counter);
    printf("That means there were %d races!\n", NUM_THREADS*NUM_ITERS - counter);
    printf("Approximately %d%% of the writes were races!\n",
           (NUM_THREADS*NUM_ITERS - counter) * 100 / NUM_THREADS / NUM_ITERS);

    // TODO: destroy the counter mutex.
    // TODO: destroy your conditional variable

    return 0;
}
