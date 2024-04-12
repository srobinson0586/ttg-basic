#include <stdio.h>
#include <string.h>

// TODO: Define a struct for a Student that has
// char name[50]
// int age
// float gpa

int main() {
    // Declare a variable of type Student
    struct Student s;

   
    printf("Enter student's name: ");
    fgets(s.name, 50, stdin);
    s.name[strcspn(s.name, "\n")] = 0; // Remove the newline character

    
    printf("Enter student's age: ");
    scanf("%d", &s.age);

    
    printf("Enter student's GPA: ");
    scanf("%f", &s.gpa);

    // TODO: Display the details of the student by accessing the values in the created struct
    

    return 0;
}