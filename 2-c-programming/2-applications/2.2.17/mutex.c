#include <stdio.h>
#include <pthread.h>

// Instructions:
// First, get the program working without using a mutex to protect
// the counter. If `counter` reaches NUM_THREADS*NUM_ITERS, there
// were no race conditions, and the program ran perfectly without
// any protections. This should happen pretty much 100% of the time
// when NUM_THREADS and NUM_ITERS are relatively low.
//
// Next, play around with increasing NUM_THREADS and NUM_ITERS,
// and see if it still runs perfectly. Record some values of these
// macros that produced a high rate of race condition errors.
//
// Finally, create a mutex and use it to protect the counter
// variable. Does this fix the issue?

// References:
// You may reference instruction videos from Jacob Sorber on how to create threads and implement 
// their various functionalities, like mutex locks during atomic operations:
// https://www.youtube.com/watch?v=uA8X5zNOGw8&t=1s [create and join threads]
// https://www.youtube.com/watch?v=9axu8CUvOKY [locks, atomic operations]


#define NUM_THREADS 100
#define NUM_ITERS   10000000

// What will this be initialized to?
int counter;

// TODO: For thread safety, create a mutex to protect the counter.
// Increment `counter` NUM_ITERS times.
void* thread_func(void* param) {
    // This will prevent gcc from complaining that `param` is an unused arg.
    (void) param;

    // TODO: Increment `counter` NUM_ITERS times, using a for loop.    
    return NULL; // TODO: Change if needed
}

int main() {
    pthread_t thread_array[NUM_THREADS] = {0};
    int create_rtn;
    int thread_idx;

    // TODO: For thread safety, initialize the counter mutex.
    // TODO: Create NUM_THREADS thread, and store their tids in thread_array.
    // TODO: Use pthread_join to wait for all threads to complete.
    // Print out information about the number of race errors.
    printf("counter = %d\n", counter);
    printf("That means there were %d races!\n", NUM_THREADS*NUM_ITERS - counter);
    printf("Approximately %d%% of the writes were races!\n",
           (NUM_THREADS*NUM_ITERS - counter) * 100 / NUM_THREADS / NUM_ITERS);

    // TODO: destroy the counter mutex.
    return 0;
}
