#pragma once

#ifdef __unix__

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

#elif defined(_WIN32) || defined(WIN32)

#include <windows.h>
#include <stdio.h>
#include <math.h>

#endif

void SectionOneOne();
void SectionOneTwo(int x, char *str);

int SectionTwoOne(int x);
int SectionTwoTwo(int x, int y);
int SectionTwoThree(int x, int y);
int SectionTwoFour(int x);
int SectionTwoFive(int x, int y);

int SectionThreeOne(int *nums, int size);
int SectionThreeTwo(int *nums, int size);
int SectionThreeThree(int *nums, int size, int index);
int SectionThreeFour(int num);
int SectionThreeFive(int **nums, int width, int height);
int SectionThreeSix(int num);

int SectionFourOne(char* str);
int SectionFourTwo(char* str, int len);
void SectionFourThree(char** dst, char* src);
void SectionFourFour(int* x, int* y);
void SectionFourFive();
int SectionFourSix(char* array);

int SectionFiveOne(char* file_name, char* str);
ssize_t SectionFiveTwo(char* file_name);
ssize_t SectionFiveThree(char* file_name, char** str);
int SectionFiveFour(char* file_name, char* str);

int SectionSixOne(int x, int y);
int SectionSixTwo(char* buf);
int SectionSixThree(FILE* stream);
