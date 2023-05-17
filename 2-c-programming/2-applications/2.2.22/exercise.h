#pragma once

#ifdef __unix__

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#elif defined(_WIN32) || defined(WIN32)

#include <windows.h>
#include <stdio.h>

#endif

// This is us declaring a struct
struct _MAKE_INFO {
	char* make;
	char* country;
};

// But writing out "struct _MAKE_INFO" every time gets a little annoying, so...
typedef struct _MAKE_INFO MAKE_INFO;
// Now we can just refer to it as "MAKE_INFO"

// Or, to write it all out in one statement:
typedef struct _WHEEL {
    char flat;
} WHEEL;

typedef struct _PERSON {
    char* name;
    char* age;
} PERSON;

typedef enum _CAR_TYPE {
    SEDAN = 4,
    SUV = 6,
    TRUCK = 2
} CAR_TYPE;

typedef struct _CAR {
	MAKE_INFO* make_info_ptr;
    CAR_TYPE type;
    WHEEL wheels[4];
    PERSON* passengers;
}CAR;

// Allocates a buffer containing an unsigned integer x followed by x car structures
// || unsigned int x | CAR | CAR | CAR |   ...   ||
char* buyMyCars();

// Fill in people structures pointed to each passenger buffer in myCarsPtr
void addPeopleToCars(CAR* myCarsPtr);