#include "exercise.h"
/*
 * Print hello world to the console.
 */
void SectionOneOne(void) {
    // TODO}

/*
 * Print "string[<index>] = <string[index]\n".
 */
void SectionOneTwo(int index, char *string) {
    // TODO}

/*
 * Return `x` + 1.
 */
int SectionTwoOne(int x) {
    // TODO    return -1;
}

/*
 * Return the result of `base` to the power of `exponent`.
 */
int SectionTwoTwo(int base, int exponent) {
    // TODO    return -1;
}

/*
 * Return the remainder of `x` / `y`
 */
int SectionTwoThree(int x, int y) {
    // TODO    return -1;
}

/*
 * Return `x` - 1.
 */
int SectionTwoFour(int x) {
    // TODO    return -1;
}

/*
 * Return the result of `x` divided by `y`.
 */
int SectionTwoFive(int x, int y) {
    // TODO    return -1;
}

/*
 * Print the address of `nums` and return the sum of all its elements.
 */
int SectionThreeOne(int *nums, int size) {
    // TODO    return -1;
}

/*
 * Return the sum of all non-negative elements `nums`.
 */
int SectionThreeTwo(int *nums, int size) {
    // TODO    return -1;
}

/*
 * Return the element in `nums` at index `index`, or -1 if `index` is
 * invalid (based on the value of `size`, which is the number of ints
 * in the array).
 */
int SectionThreeThree(int *nums, int size, int index) {
    // TODO    return -1;
}

/*
 * Return 1 if `n` is a prime number; 0 otherwise.
 */
int SectionThreeFour(int n) {
    // TODO    return -1;
}

/*
 * Return the sum of all values in the 2-D array `nums`.
 *
 * `nums` is a pointer to an array of `height` integer pointers.
 * Each of those integer pointers holds the address of an array of
 * `width` integers.
 */
int SectionThreeFive(int** nums, int width, int height){
    // TODO    return -1;
}

/*
 * Use a switch statement to match on `num` and print the correct
 * string, according to the following pairing:
 *   1: "This is "
 *   2: "order\n"
 *   3: "the correct "
 */
int SectionThreeSix(int num){
    // TODO    return -1;
}

/*
 * Return 1 if `str` is "p01n73rz"; return 0 otherwise.
 */
int SectionFourOne(char* str) {
    // TODO    return -1;
}

/*
 * Compare `str` to "p01n73rz" for `len` characters; return 1 if they
 * match and 0 if they don't.
 */
int SectionFourTwo(char* str, int len) {
    // TODO    return -1;
}

/*
 * Copy the string `src` to the destination `*dst`.
 *
 * The caller must make sure that `*dst` has enough space to hold the
 * string from `src`.
 */
void SectionFourThree(char** dst, char *src) {
    // TODO}

/*
 * Multiply the integers pointed to by `x` and `y` by 5.
 */
void SectionFourFour(int* x, int *y) {
    // TODO}

/* Create an array of five strings of your choosing and print each
 * element to the console with the format "array[<idx>] = <string>".
 */
void SectionFourFive() {
    // TODO}

/* Read the 4 bytes pointed to by `array` and interpret them as an int
 * in little-endian format. Return that integer value, incremented by 1.
 */
int SectionFourSix(char* array) {
    // TODO}

/*
 * Create a file with name `file_name` and write `str` to it.
 * Return 0 on success and -1 on failure.
 */
int SectionFiveOne(char* file_name, char* str) {
    // TODO    return -1;
}

/*
 * Return the size of the file named `file_name` (in bytes), or -1 if
 * `file_name` doesn't exist.
 */
ssize_t SectionFiveTwo(char* file_name) {
    // TODO    return -1;
}

/*
 * Read the contents of a file into an newly allocated buffer and
 * return the size of that buffer.
 *
 * This function reads the contents of the file named `file_name`.
 * It allocates a buffer (`*str`) big enough to hold all the contents
 * and copies the contents into that buffer.
 * The contents of `*str` must be null-terminated.
 * It returns the size of the buffer it allocated, or -1 on failure.
 */
ssize_t SectionFiveThree(char* file_name, char** str) {
    // TODO    return -1;
}

/*
 * (1) Create a new file named `file_name` and write the string `str`
 *     to it. Then close the file.
 * (2) Re-open the file, and change the first character to a "b". Then
 *     close the file.
 * (3) Re-open the file, and write `str` to the end of it. Then close
 *     the file.
 * (4) Find the size of the file.
 * (5) Delete the file.
 * (6) Return the size of the file.
 *
 * NOTE: Pay careful attention to the mode you're using to open the
 *       file each time. This is one of the main points of this problem.
 */
int SectionFiveFour(char* file_name, char* str){
    // TODO    return -1;
}

/*
 * Generate a random integer in the range [`x`, `y`).
 * `x` and `y` shall not be negative.
 *
 * The range [`x`, `y`) means integers greater than or equal to `x`
 * and less than `y`.
 * Return the random integer, or -1 if the bounds are invalid (i.e., if
 * `x` >= `y`) or if either `x` or `y` is negative.
 *
 * NOTE - The verifier will call `srand`; do not do this again.
 * NOTE - Do not call `rand` if the range is invalid.
 */
int SectionSixOne(int x, int y) {
    // TODO    return -1;
}

/*
 * Convert a string (in base 10) to a non-negative integer.
 *
 * Your function should return -1 if the string:
 * - has any non-numeric characters (besides trailing whitespace),
 * - has no non-whitespace characters,
 * - represents a floating point number,
 * - represents a value greater than RAND_MAX, or
 * - represents a negative integer.
 */
int SectionSixTwo(char *buf) {
    // TODO
    return -1;
}

/*
 * Read 2 integers from the file pointer `stream` and return a random
 * number in the range between them. Return -1 if the bounds are
 * invalid (just as for SectionSixOne).
 *
 * `stream` contains 2 strings representing integers in base 10. These
 * 2 strings are on their own lines (i.e., each followed by a newline).
 * Read the lines from the file using `getline`, and then use the 2
 * functions above to complete this function.
 */
int SectionSixThree(FILE *stream) {
    // TODO    return -1;
}
