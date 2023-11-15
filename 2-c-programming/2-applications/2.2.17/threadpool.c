#include <pthread.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define NUM_THREADS 100
#define NUM_ITERS   10000000


// Instructions: 
// Take your code from conditionals.c and incorporate thread pools to increment 
// and decrement 'counter'. For now, decrement when 'counter' > 14
// Note: you'll have to edit some of your original functions and add 
// additional functions to be able to complete this task

// You may use the following reference to familiarize yourself with thread pools
// https://www.youtube.com/watch?v=_n2hE2gyPxU


// TODO: For thread safety, create a mutex variable to protect the counter (pthread_mutex_t)
// TODO: For condition safety, create a conditional variable (pthread_cond_t)

// What will this be initialized to?
int counter;

// TODO: initialize a task queue
// TODO: initialize task count


// TODO: implement function that waits and gets task from queue
void* startThread(void* args)
{
    // TODO: set mutex lock
    return NULL; // TODO: Change if needed
}

// TODO: submit task function ... add a thread into the queue
void submitTask(int* t) 
{
    // TODO: set mutex lock
}

// TODO: Implement your 'executeTask' function: Increment `counter` NUM_ITERS times.
void inc_task(int* param) {


    // TODO: Increment `counter` NUM_ITERS times, using a for loop.    return 0;

    
    // TODO: set your signal objects here
}

// Decrement `counter` NUM_ITERS times.
void dec_task(int* param) {

    // TODO: Decrement `counter` NUM_ITERS times, using a for loop.    return 0;

    // TODO: set mutex locks
    
    // TODO: set signal object
}

int main() {
    pthread_t thread_array[NUM_THREADS] = {0};
    int create_rtn;
    int thread_idx;

    // TODO: Initialize the counter mutex.
    // TODO: initialize the conditional variable


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
