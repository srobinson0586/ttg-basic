#include <stdio.h>
#include <string.h>
#include "cs50.h"

// Define a constant for the maximum number of students
#define MAX_STUDENTS 50

// TODO: Define a function called 'inputStudentData' that takes arrays for names and scores,
//       and the index of the student as parameters.
//       This function should prompt the user to enter the name and score of the student
//       at the specified index, and store them in the arrays.


// TODO: Define a function called 'highestScoreIndex' that takes an array of scores,
//       an array of names, and the number of students as parameters.
//       This function should return the index of the highest score in the array.


int main() {
    char names[MAX_STUDENTS][50];
    int scores[MAX_STUDENTS];
    int numStudents;

    // TODO: Prompt the user to enter the number of students (less than or equal to MAX_STUDENTS)
    

    // TODO: Read the number of students entered by the user and store it in the variable 'numStudents'
    

    // TODO: Loop through each student and call the 'inputStudentData' function to input their data
    

    // TODO: Call the 'highestScoreIndex' function with the arrays of scores and names, and the number of students
    //       and store the index of the highest score in a variable
    

    // TODO: Print the name(s) of the student(s) with the highest score using the index obtained above
    

    return 0;
}

// Define the 'inputStudentData' function as per the TODO instructions above
void inputStudentData(char names[][50], int scores[], int index) {
    // Your code here
}

// Define the 'highestScoreIndex' function as per the TODO instructions above
int highestScoreIndex(int scores[], int numStudents) {
    // Your code here
}
