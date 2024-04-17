#pragma once

#ifdef __unix__

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#elif defined(_WIN32) || defined(WIN32)

#include <windows.h>
#include <stdio.h>

#endif

/* student struct
 */
typedef struct _student {
	// TODO: student id variable
	char *student_id;
	// TODO: student name variable
	char *student_name;
	// TODO: hacker name variable
	char *hacker_name;
} student;

/* 
 * Linked list struct
 */
typedef struct _node {
	// TODO: pointer to student struct
	student *my_student;
	// TODO: pointer to next node
	struct _node *next;
} node;

void wc(char *buf, size_t len);
void cat(char *buf, size_t len);
void help();
void studentPrint();
void studentInfo();
void addStudent(student *s);
void cleanupList();
void trimNewline(char *buf); // optional
void illFormatted(char *buf); // optional
void trimSpace(char *buf); // optional