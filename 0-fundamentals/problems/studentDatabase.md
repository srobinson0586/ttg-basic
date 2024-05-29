## Student Database System

**Objective:**
Create a simple student database system that allows the user to add new student records, display all student records, and search for a student by their ID. Each student record should contain the student's ID, name, and GPA.
Requirements:
1. Struct Definition: Define a struct named Student that contains three fields:
int id for the student's ID.
char name[100] for the student's name.
float gpa for the student's GPA.


2. Global Array of Structs: Define a global array that can hold up to 50 Student structs. This will act as your in-memory database.
3. Functions:
   - Add Student: Write a function void addStudent(int* count) that takes a pointer to the current count of students in the database. This function should prompt the user to enter the details for a new student (ID, name, and GPA) and add the new student to the array. Increment the count of students accordingly.
   - Display All Students: Write a function void displayStudents(int count) that takes the current count of students and displays the details of all students in the database.
   - Search for Student by ID: Write a function void searchStudentById(int count) that asks the user for a student ID, searches for the student in the database, and displays the student's details if found. If the student is not found, it should print a message indicating so.
4. Main Function:
   - Your main function should present a simple menu to the user with options to add a student, display all students, search for a student by ID, and exit the program.
   - Use a loop to keep the program running until the user chooses to exit.
   - Make sure to use the functions you've defined for each operation.


Sample Menu:
```
1. Add Student 
2. Display All Students 
3. Search for Student by ID 
4. Exit Enter your choice: 
```

/*
Student Database System

Objective:
Create a simple student database system that allows the user to add new student records, display all student records, and search for a student by their ID. Each student record should contain the student's ID, name, and GPA.

Requirements:
1. Struct Definition: Define a struct named Student that contains three fields:
   - int id for the student's ID.
   - char name[100] for the student's name.
   - float gpa for the student's GPA.

2. Global Array of Structs: Define a global array that can hold up to 50 Student structs. This will act as your in-memory database.

3. Functions:
   - Add Student: Write a function void addStudent(int* count) that takes a pointer to the current count of students in the database. This function should prompt the user to enter the details for a new student (ID, name, and GPA) and add the new student to the array. Increment the count of students accordingly.
   - Display All Students: Write a function void displayStudents(int count) that takes the current count of students and displays the details of all students in the database.
   - Search for Student by ID: Write a function void searchStudentById(int count) that asks the user for a student ID, searches for the student in the database, and displays the student's details if found. If the student is not found, it should print a message indicating so.

4. Main Function:
   - Your main function should present a simple menu to the user with options to add a student, display all students, search for a student by ID, and exit the program.
   - Use a loop to keep the program running until the user chooses to exit.
   - Make sure to use the functions you've defined for each operation.

Sample Menu:
1. Add Student 
2. Display All Students 
3. Search for Student by ID 
4. Exit 
Enter your choice:
*/

#include <stdio.h>

// Struct Definition

// Global Array of Structs

// Function to Add Student

// Function to Display All Students

// Function to Search for Student by ID

// Main Function
