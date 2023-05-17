#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>

// Overview:
//
// This program creates NUM_THREADS threads, each with a status
// contained in thread_status_array.
// Each thread needs to change its status from Pending to Active,
// wait 1 second, and then change it to Finished.
// To simulate a resource-constrained system, we want to allow a
// maximum of MAX_ACTIVE threads to have an Active status at any
// given time.
// Follow the TODO statements to complete the project.

#define NUM_THREADS 20
#define MAX_ACTIVE  5

enum thread_status {
    Pending,
    Active,
    Finished
};

enum thread_status thread_status_array[NUM_THREADS];

// TODO: Declare a semaphore.
// TODO:
// Set the correct element of thread_status_array to Active,
// wait 1 second, and then set it to Finished.
// The argument `param` is the thread index, cast to a (void*).
// Include semaphore operations to limit the number of Active
// threads to MAX_ACTIVE.
void* thread_func(void* param) {    return NULL;
}

int main() {
    pthread_t thread_array[NUM_THREADS] = {0};
    long thread_idx;

    // Initialize all thread statuses to Pending.
    for (thread_idx = 0; thread_idx < NUM_THREADS; thread_idx++) {
        thread_status_array[thread_idx] = Pending;
    }

    // TODO: Initialize the semaphore to limit the number of active
    // threads to MAX_ACTIVE.
    // TODO: Create NUM_THREADS threads and store the tids in thread_array.
    // This block of code will continuously monitor thread_status_array
    // and print out an update when the number of active threads changes.
    // It will break when all threads are marked as Finished.
    int prev_active = 0;
    int active;
    int waiting_on_at_least_one_thread = 1;
    while (waiting_on_at_least_one_thread) {
        active = 0;
        waiting_on_at_least_one_thread = 0;
        for (thread_idx = 0; thread_idx < NUM_THREADS; thread_idx++) {
            if (thread_status_array[thread_idx] != Finished) {
                waiting_on_at_least_one_thread = 1;
            }
            if (thread_status_array[thread_idx] == Active) {
                active++;
            }
        }
        if (active != prev_active) {
            printf("There are now %d threads active!\n", active);
            prev_active = active;
        }
    }

    // TODO: Use pthread_join to wait for all threads to complete.
    // TODO: Destroy the semaphore.
    return 0;
}
