#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

extern typeof(getline) student_getline;

#define NEWLINE_LIMIT 0x1000

// Write semi-random characters to a file to make a good test
// case for getline.
void write_random_file(const char* filename) {
    srand((unsigned int) time(NULL));

    FILE* f = fopen(filename, "w");
    int c;
    size_t count = 0;

    while (1) {
        // Write a random lowercase letter or newline to the file.
        c = rand() % NEWLINE_LIMIT;
        if (c == NEWLINE_LIMIT - 1) {
            c = '\n';
        } else {
            c = (c % 26) + 0x61;
        }
        fputc(c, f);

        // Possibly break after 0x100 iterations.
        if (count > 0x100) {
            if ((rand() & 0xffff) == 0) {
                break;
            }
        }
        count++;
    }
    fclose(f);
}

int test(char* filename) {
    int pass = 1;

    // Open the same file twice.
    FILE* student_f = fopen(filename, "r");
    FILE* libc_f = fopen(filename, "r");

    char* student_lineptr = NULL;
    char* libc_lineptr = NULL;

    size_t student_size = 0;
    size_t libc_size = 0;

    ssize_t student_rtn = 0;
    ssize_t libc_rtn = 0;

    while (1) {
        student_rtn = student_getline(&student_lineptr, &student_size, student_f);
        libc_rtn = getline(&libc_lineptr, &libc_size, libc_f);

        if (student_rtn != libc_rtn) {
            printf("Return values disagree! Yours (%zd) != libc's (%zd)\n",
                   student_rtn, libc_rtn);
            pass = 0;
            break;
        } else if (libc_rtn == -1) {
            break;
        } else if (strcmp(student_lineptr, libc_lineptr) != 0) {
            printf("Your line is incorrect!\n");
            printf("You read:  '%s'\n", student_lineptr);
            printf("libc read: '%s'\n", libc_lineptr);
            pass = 0;
            break;
        } else if (student_size <= (size_t) libc_rtn) {
            printf("You allocated only (%zd) bytes on the heap, which doesn't"
                   " leave room for a null byte after %zd chars read.\n",
                   student_size, libc_rtn);
            pass = 0;
            break;
        }
    }
    free(student_lineptr);
    free(libc_lineptr);
    fclose(student_f);
    fclose(libc_f);
    return pass;
}

int main(int argc, char** argv) {
    char* filename = "test.txt";

    if (argc == 2) {
        if (strcmp(argv[1], "rand") == 0) {
            filename = "rand.txt";
            write_random_file("rand.txt");
        }
    }

    printf("Running tests on %s\n", filename);

    if (test(filename)) {
        printf("Congratulations! Your implementation passed the tests!\n");
    } else {
        printf("Sorry, your implementation failed :(\n");
    }

    return 0;
}
