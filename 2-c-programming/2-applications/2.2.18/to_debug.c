#ifdef __unix__

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#elif defined(_WIN32) || defined(WIN32)

#include <windows.h>
#include <stdio.h>

#endif

void func(int * x){
    *x = 2000;
}

typedef struct _strings{
    char a[24];
    char * b;
} strings;

int main(int argc, char * argv[]){

    int x = 5;
    int z = 10;
    void * y = (void *) &x;

    char * string = "1234567890123456789";

    func(y);

    func((int *)z); //WRONG

    strings s = {0};

    s.b = string;

    //s.a = string;

    if(strncmp(s.b, s.a, strlen(string))==0){
        printf("SUCCESS!\n");
    }

    return 0;
}