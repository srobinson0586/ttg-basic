#include "shell.h"

#define MAX_SIZE 64

node *student_list = NULL; // list to keep track of students

/*
 * Frees all dynamically allocated buffers in student_list
 * Params: none
 * Return: none
 */
void cleanupList() {
	// TODO: free memory in student_list

}

/*
 * Prompt user to input student information
 * Params: none
 * Return: none
 */
void studentInfo() {
	// TODO: dynamically allocate student struct to add to linked list

	printf("student id: ");
	// TODO: prompt user to input student id


	printf("student name: ");
	// TODO: prompt user to input student name

	printf("hacker name: ");
	// TODO: prompt user to input hacker name

	// TODO: call addStudent to add student to student_list
}

/*
 * Add student information to student_list
 * Params:
 * 	student *s - pointer to struct with student information
 * Return: none
 */
void addStudent(student *s) {
	// TODO: create node to hold s
	// TODO: add s to student_list
}

/*
 * Prints student information in student_list
 * Params: none
 * Return: none
 */
void studentPrint() {
	// TODO: print if there are no students have been added to student_list
	// TODO: iterate through student_list and print all student information
}

/* Implements cat
 * Params:
 * 	char *cmd_buf - shell command
 * 	size_t buf_len - size of shell command
 * Return:
 * 	none
 */
void cat(char *cmd_buf, size_t buf_len) {
	// TODO: implement cat	
}

/* Implements wc
 * Params:
 * 	char *cmd_buf - shell command
 * 	size_t buf_len - size of shell command
 * Return:
 * 	none
 */
void wc(char *cmd_buf, size_t buf_len) {
	// TODO: implement wc

}

/* Prints help information
 * Params: none
 * Return: none
 */
void help() {
	printf("51mpl3 5h3ll welcomes you\n");
	printf("the traditional shell commands you are responsible for implementing are:\n\t> wc\n\t> cat\n\t> exit\n");
	printf("if you are unfamiliar with these shell commands, use the man pages\n");
	printf("all files for cat and wc commands will be in the current directory\n");
	printf("implementations do not have to include flags\n");
	printf("your shell should run until you type \'exit\'\n\n");
	printf("you will also need to implement a shell command called \'student\'\n");
	printf("student will prompt the user to enter the following:\n\t1. student id\n\t2. student name\n\t3. hacker name\n");
	printf("\nyou will also need to print the student information\ndo this with the shell command \'student print\'\nwhen the command is run it will print the information for all the students that have been added\n"); 
	printf("indicate if the user inputs a command other than wc, cat, student, student print, or exit\n");
	printf("\nimplementation for all commands should look like:\n\n");
	printf("$ cat text.txt\nsh3llz are\nfunnn\nlike\nthe most\nfunnn!\n");
	printf("$ wc text.txt\n 5  7 38 text.txt\n");
	printf("$ ls\nls: command not found\n");	
	printf("$ student print\nno students in list\n");
	printf("$ student\nstudent id: 123\nstudent name: linux\nhacker name: tux\n");
	printf("$ student print\n---STUDENT-01---\nstudent id: 123\nstudent name: linux\nhacker name: tux\n");
	printf("$ exit\n\n");
	printf("let\'s begin...\n\n\n");
}

void trimNewline(char *buf) {
	for(int i = 0; ; i++) {
		if(buf[i] == '\n') {
			buf[i] = '\0';
			break;
		}
	}
}

void trimSpace(char *buf) {
	size_t i;
	for(i = 1; i < strlen(buf) + 1; i++) { // trims annoying space that gets left on...
		buf[i-1] = buf[i];
	}
}

void illFormatted(char *buf) {
	printf("s1mpl3 sh3ll: ill formatted %s command\n", buf);
}
