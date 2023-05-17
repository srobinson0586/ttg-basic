#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "exercise.h"
#include "blackbox.h"

#define PASS 0
#define FAIL -1

#define NUM_TESTS 10

int MyRand(void) {
    return (rand() % 2000) - 1000;
}

int TestBlackBox(void) {
    int rtn = PASS;
    int i;
    int a, b;
    for (i = 0; i < NUM_TESTS; i++) {
        a = MyRand();
        b = MyRand();
        if (BlackBox(a, b) != ((a + b) ^ (a - b))) {
            rtn = FAIL;
            break;
        }
    }
    return rtn;
}

int TestSumFiveArgs(void) {
    int rtn = PASS;
    int i;
    int a, b, c, d, e;
    for (i = 0; i < NUM_TESTS; i++) {
        a = MyRand();
        b = MyRand();
        c = MyRand();
        d = MyRand();
        e = MyRand();
        if (SumFiveArgs(a, b, c, d, e) != a + b + c + d + e) {
            rtn = FAIL;
            break;
        }
    }
    return rtn;
}

int TestFunc2(void) {
    int rtn = PASS;
    int i;
    int a, b, c, d;
    for (i = 0; i < NUM_TESTS; i++) {
        a = MyRand();
        b = MyRand();
        c = MyRand();
        d = MyRand();
        if (Func2(a, b, c, d) != a + b + BlackBox(c, d)) {
            rtn = FAIL;
            break;
        }
    }
    return rtn;
}

int main(void) {
    srand((unsigned)time(NULL));

    printf("SunFiveArgs @ %p\nSumFiveArgsSize @ %p\n", SumFiveArgs, &SumFiveArgsSize);
    printf("Func2 @ %p\nFunc2Size @ %p\n", Func2, &Func2Size);

    if (TestBlackBox() == PASS) {
        puts("Verified that BlackBox works.");
    }
    else {
        puts("Error: BlackBox is failing. Go tell the traino he messed up.");
        return -1;
    }

    if (TestSumFiveArgs() == PASS) {
        printf("SumFiveArgs passed (using %d bytes)!\n", SumFiveArgsSize);
    }
    else {
        puts("Error: SumFiveArgs failed. Use WinDbg to fix your bug.");
        return -1;
    }

    if (TestFunc2() == PASS) {
        printf("Func2 passed (using %d bytes)!\n", Func2Size);

    }
    else {
        puts("Error: Func2 failed. Use WinDbg to fix your bug.");
        return -1;
    }

    puts("Congrats! You finished the Windows assembly programming project!");
    return 0;
}
