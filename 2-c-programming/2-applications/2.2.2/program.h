#ifdef __unix__

#include <stdlib.h>
#include <stdio.h>

#elif defined(_WIN32) || defined(WIN32)

#include <windows.h>
#include <stdio.h>

#endif


#ifndef PROGRAM_H_
#define PROGRAM_H_

#define BUFSIZE 1024

struct point
{
    int x;
    int y;
};

struct shape
{
    struct point edge1;
    struct point edge2;
    struct point edge3;
    struct point edge4;
};

int readInput(char *buf, int size, int *bytesRead);
void *welcomeMessage();
void exitProgram(int exitVal);
void createRectangle(struct shape *rectangle);
struct point createPoint(int x, int y);
int calcArea(struct shape *rectangle);

#endif /* PROGRAM_H_ */
