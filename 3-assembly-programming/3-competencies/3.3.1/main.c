#ifdef __unix__

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>

#elif defined(_WIN32) || defined(WIN32)

#include <windows.h>
#include <stdio.h>

#endif

extern int lab1_1(int a, int b);
extern int lab1_2(int a);
extern int lab1_3(int a, int b);
extern int lab1_4(int a, int b, int c, int d);
extern int lab1_5(int a, int b);
extern int lab1_6(int *a);
extern unsigned int lab1_7(unsigned int a);
extern int lab2_1(int a, int b);
extern int lab2_2(int a, int b);
extern int lab2_3(int a, int b, int c, int d);
extern int lab2_4(int a);
extern void lab3_1(char *userStr);
extern int lab3_2(char *userStr);
extern void lab3_3(char *dst, char *src, int strLen);
extern void lab3_4(int strLen, char *dst, char *src);
extern void lab3_5(char *filePath, char *writeStr, int strLen);
extern void optional_1(char *dst, char *src);
extern void optional_2(char *src, int strLen);

void verifyLab1_1();
void verifyLab1_2();
void verifyLab1_3();
void verifyLab1_4();
void verifyLab1_5();
void verifyLab1_6();
void verifyLab1_7();
void verifyLab2_1();
void verifyLab2_2();
void verifyLab2_3();
void verifyLab2_4();
void verifyLab3_1();
void verifyLab3_2();
void verifyLab3_3();
void verifyLab3_4();
void verifyLab3_5();
void verifyOpt1();
void verifyOpt2();

int main(){
    printf("Welcome to the Assembly Verifier!\n");
    printf("Please only use instructions covered up until this point\n\n");

    // Arithmetic Section
    verifyLab1_1();
    verifyLab1_2();
    verifyLab1_3();
    verifyLab1_4();
    verifyLab1_5();
    verifyLab1_6();
    verifyLab1_7();
    // Control Flow Section
    verifyLab2_1();
    verifyLab2_2();
    verifyLab2_3();
    verifyLab2_4();
    // Misc (Strings, Extern, Syscalls, etc.)
    verifyLab3_1();
    verifyLab3_2();
    verifyLab3_3();
    verifyLab3_4();
    verifyLab3_5();
    printf("Assembly verifier complete.\nAll test cases pass.\n\n\nUncomment the verifyOpt1() and verifiyOpt2() in main to check the optional functions.\n");
    // Optional
    // verifyOpt1();
    // verifyOpt2();

    return 0;
}

void verifyLab1_1(){
    int a[] = {3, 5, 7};
    int b[] = {5, 20, 40};
    int result = 0;

    for(uint i = 0; i < sizeof(a)/sizeof(a[0]); i++) {
    	result = lab1_1(a[i], b[i]);

    	if(result != (a[i] * b[i])) {
            printf("Lab1_1 Fail!\nreturned: %d\nexpected: %d\n", result, a[i]*b[i]);
    	    exit(0);
    	}
    }
    printf("Lab1_1 Pass!\n");
}

void verifyLab1_2(){
    int result = 0;
    int c[] = {1, 2, 3, 4, 5};
    for(int d = 0; d < 5; d++){
        result = lab1_2(c[d]);
        if(result != (c[d] * 8)) {
            printf("Lab1_2 Fail!\nreturned: %d\nexpected: %d\n", result, c[d] * 8 );
            exit(0);
        }
    }
    printf("Lab1_2 Pass!\n");
}

void verifyLab1_3(){
    unsigned long a[] = {5, 0, 12};
    unsigned long b[] = {10, 54, 31};
    unsigned long c = 0, d = 0;

    for(uint i = 0; i < sizeof(a)/sizeof(a[0]); i++) {
        c = 0;
        d = 0;
        asm(
	    "mov %[n], %%rcx;\n\t"
	    "mov %[o], %%rdx;\n\t"
	    "call lab1_3;\n\t"
	    "mov %%rcx, %[c];\n\t"
	    "mov %%rdx, %[d];\n\t"
	    : [c]"=c"(c), [d]"=d"(d)
	    : [n]"rm"(a[i]), [o]"rm"(b[i])
	    :);
    	if(!(( c == b[i]) && (d == a[i]))) {
            printf("Lab1_3 Fail!\nreturned: %ld and %ld\nexpected: %ld and %ld\n", c, d, b[i], a[i]);
    	    exit(0);
    	}
    }
    printf("Lab1_3 Pass!\n");
}

//12 * 4(rdi) / 2(rcx) + 6(rsi) = 30(rdx)
//2 * 12(rdi) / 6(rcx) + 45(rsi) = 49(rdx)
//8 * 5(rdi)/ 4(rcx) + 3(rsi) = 13(rdx)
void verifyLab1_4(){
    int a[] = {4, 12, 5};
    int b[] = {6, 45, 3};
    int c[] = {30, 49, 13};
    int d[] = {6, 6, 4};
    int result = 0;

    for(uint i = 0; i < sizeof(a)/sizeof(a[0]); i++) {
    	result = lab1_4(a[i], b[i], c[i], d[i]);
    	if(result != ((c[i] - b[i]) * d[i]/ a[i])) {
           printf("Lab1_4 Fail!\nreturned: %d\nexpected: %d\n", result, 59);
    	    exit(0);
       }
    }
    printf("Lab1_4 Pass!\n");
}


void verifyLab1_5(){
    int a[] = {0x1200, 0xcaff, 0x1334};
    int b[] = {0x0034, 0xfffe, 0x2237};
    int result = 0;

    for(uint i = 0; i < sizeof(a)/sizeof(a[0]); i++){
        //printf("0x%x and 0x%x\n Added Equals: 0x%x\n", (a[i] & 0xff00), (b[i] & 0xff), (a[i] & 0xff00) + (b[i] & 0xff));
        result = lab1_5(a[i], b[i]);
        if(result != (a[i] & 0xff00) + (b[i] & 0xff)){
            printf("Lab1_5 Fail!\nreturned: 0x%x\nexpected: 0x%x\n", result, (a[i] & 0xff00) + (b[i] & 0xff));
            exit(0);
        }
    }
    printf("Lab1_5 Pass!\n");
}

void verifyLab1_6(){
    int a[] = {55, 85, 13546};
    int result = 0;
    int *intPtr = NULL;

    for(uint i = 0; i < sizeof(a)/sizeof(a[0]); i++) {
    	intPtr = &(a[i]);
    	result = lab1_6(intPtr);
        if(result != (a[i] - 20)) {
            printf("Lab1_6 Fail!\nreturned: %d\nexpected: %d\n", result, a[i] - 20);
    	    exit(0);
    	}
    }
    printf("Lab1_6 Pass!\n");
}

void verifyLab1_7(){
    // Swap the following number from 0x12345678 to 0x78563412
    // (Equivalent to htonl).
    unsigned int a = 0x12345678;
    unsigned int correct_result = 0x78563412;
    unsigned int result = lab1_7(a);
    if(result != correct_result){
        printf("Lab1_7 Fail!\nreturned: %x\nexpected: %x\n", result, correct_result);
        exit(0);
    }
    printf("Lab1_7 Pass!\n");
}

void verifyLab2_1(){
    unsigned int c = 0, b = 0;
    unsigned int d[] = {17, 3, 0};
    unsigned int s[] = {13, 17, 3};
    for(uint i = 0; i < sizeof(d)/sizeof(d[0]); i++){
        asm(
            "mov %[d], %%edi;\n\t"
            "mov %[s], %%esi;\n\t"
            "call lab2_1;\n\t"
            "mov %%ecx, %[c];\n\t"
            "mov %%ebx, %[b];\n\t"
            : [c]"=c"(c), [b]"=b"(b)
            : [d]"rm"(d[i]), [s]"rm"(s[i])
            :);
        if(d[i] == 0){
            if(c != 100){
                printf("Lab2_1 Fail!\nrcx returned: %d\nrcx expected: %d\n", c, 100);
                exit(0);
            }
            continue;
        }
        if(d[i] == 17){
            if(b != 1){
  	        printf("Lab2_1 Fail!\nrbx returned: %d\nrbx expected: %d\n", b, 1);
                exit(0);
            }
        }
        else{
	    if(b != 2){
		printf("Lab2_1 Fail!\nrbx returned: %d\nrbx expected: %d\n", b, 2);
	        exit(0);
	    }
        }
        if(s[i] == 17){
	    if(c != 1){
                printf("Lab2_1 Fail!\nrcx returned: %d\nrcx expected: %d\n", c, 1);
                exit(0);
            }
        }
	else{
	    if(c != 2){
                printf("Lab2_1 Fail!\nrcx returned: %d\nrcx expected: %d\n", c, 2);
                exit(0);
	    }
        }
    }
    printf("Lab2_1 Pass!\n");
}

void verifyLab2_2(){
    unsigned int n = 0, o = 0;
    unsigned int d[] = {8, 10, 10};
    unsigned int s[] = {32, 5, 10};
    for(uint i = 0; i < sizeof(d)/sizeof(d[0]); i++){
        asm(
            "mov %[d], %%edi;\n\t"
            "mov %[s], %%esi;\n\t"
            "call lab2_2;\n\t"
            "mov %%edi, %[n];\n\t"
            "mov %%esi, %[o];\n\t"
            : [n]"=D"(n), [o]"=S"(o)
            : [d]"rm"(d[i]), [s]"rm"(s[i])
            :);
	do{
            s[i] = s[i] * 2;
	    d[i] = d[i] * 3;
        }while(s[i] > d[i]);
        if((s[i] != o) || (d[i] != n)){
            printf("Lab2_2 Fail!\nreturned (rsi, rdi): (%d, %d)\nexpected (rsi, rdi): (%d, %d)\n", o, n, s[i], d[i]);
            exit(0);
        }
    }
    printf("Lab2_2 Pass!\n");
}

void verifyLab2_3(){
    int result = 0;
    int rdi[] = {6, 4, 2, 3, 1};
    int rcx = 0, rsi = 0, rdx = 0;

    for(uint i = 0; i < sizeof(rdi)/sizeof(rdi[0]); i++){
    	rcx = 45;
    	rsi = 73;
    	rdx = 54;
        result = lab2_3(rdi[i], rsi, rdx ,rcx);
        switch(rdi[i]){
            case 1:
                if(result != (rdx + 42)){
                    printf("Lab2_3 Fail!\ncase: %d\nreturned: %d\nexpected %d\n", rdi[i], result, rdx + 42);
                    exit(0);
                }
                break;
            case 2:
                if(result != 0){
                    printf("Lab2_3 Fail!\ncase: %d\nreturned: %d\nexpected: %d\n", rdi[i], result, 0);
                    exit(0);
                }
                break;
            case 3:
            case 4:
                if(result != (rsi - rcx)){
                    printf("Lab2_3 Fail!\ncase: %d\nreturned: %d\nexpected: %d\n", rdi[i], result, rsi - rcx);
                    exit(0);
                }
                break;
            default:
                if(result != 50){
                    printf("Lab2_3 Fail!\ncase: default\nreturned: %d\nexpected: %d\n", result, 50);
                    exit(0);
                }
        }
    }
    printf("Lab2_3 Pass!\n");
}

void verifyLab2_4(){
    int rdi[] = {100, 6, 764, 17, 999};
    int result = 0;
    int count = 0;
    int divCount = 0;
    for(uint i = 0; i < sizeof(rdi)/sizeof(rdi[0]); i++){
        result = lab2_4(rdi[i]);
        while(count != rdi[i]){
            count += 1;
            if((rdi[i] % count) == 0){
                divCount += 1;
            }
        }
        if(divCount != result){
            printf("Lab2_4 Fail!\ncase: %d\nreturned: %d\nexpected: %d\n", rdi[i], result, divCount);
            exit(0);
        }
        divCount = 0;
        count = 0;
    }
    printf("Lab2_4 Pass!\n");
}

void verifyLab3_1(){
    size_t len = strlen("Heyo") + 1;
    char *myPtr = calloc(1, len);
    strncpy(myPtr, "Heyo", len);
    lab3_1(myPtr);
    if(strncmp(myPtr,"Heya", len) != 0) {
        printf("Lab3_1 Fail!\nreturned: %s\nexpected: %s\n", myPtr, "Heya");
    	free(myPtr);
	exit(0);
    }
    printf("Lab3_1 Pass!\n");
    free(myPtr);
}

void verifyLab3_2(){
    char *strBank[] = {"Test", "Longer Test", "Longest Test"};
    int result = 0;
    char *myPtr = NULL;
    size_t len = 0;

    for(uint i = 0; i < sizeof(strBank)/sizeof(strBank[0]); i++){
        len = strlen(strBank[i]) + 1;
        myPtr = calloc(1, len);
        strncpy(myPtr, strBank[i], len);
        result = lab3_2(strBank[i]);
        if((size_t) result != len - 1){
            printf("Lab3_2 Fail!\ncase: %s\nreturned: %d\nexpected: %ld\n", strBank[i], result, len - 1);
            free(myPtr);
	    exit(0);
        }
        free(myPtr);
    }
    printf("Lab3_2 Pass!\n");
}

void verifyLab3_3(){
    char *testStrs[] = {"Loop", "Tonka", "TApe Recorder"};
    char *ansStrs[] = {"LOOp", "TOnkA", "TApe RecOrder"};
    char *src = NULL;
    char *dst = NULL;
    size_t len = 0;
    for(uint i = 0; i < sizeof(testStrs)/sizeof(testStrs[0]); i++){
	len = strlen(testStrs[i]) + 1;
        src = calloc(1, len);
        dst = calloc(1, len);

        strncpy(src, testStrs[i], len);
        lab3_3(dst, src, len - 1);

        if(strncmp(dst, ansStrs[i], strlen(ansStrs[i]) + 1) != 0){
            printf("Lab3_3 Fail!\ncase: %s\ndst: %s\nexpected: %s\n", testStrs[i], dst, ansStrs[i]);
            free(src);
	    free(dst);
	    exit(0);
        }
        free(src);
        free(dst);
    }
    printf("Lab3_3 Pass!\n");
}

void verifyLab3_4(){
    char *testStrs[] = {"JQR", "ASM Dev", "Easy Copy"};
    //char *src = NULL;
    char *dst = NULL;
    size_t len = 0;
    for(uint i = 0; i < sizeof(testStrs)/sizeof(testStrs[0]); i++){
        len = strlen(testStrs[i]) + 1;
        //src = calloc(1, len);
        dst = calloc(1, len);
        lab3_4(len - 1, dst, testStrs[i]);

        if(strncmp(testStrs[i], dst, len) != 0){
            printf("Lab3_4 Fail!\ndst: %s\nexpected: %s\n", testStrs[i], dst);
            free(dst);
            exit(0);
        }
        //free(src);
        free(dst);
    }
    printf("Lab3_4 Pass!\n");
}

void verifyLab3_5(){
    FILE *fp = NULL;
    char *filePath = "./test.txt";
    char *myStr = "Congratulations! on Finishing the Assembly Verifier!";
    int len = strlen(myStr) + 1;
    ssize_t read = 0;
    size_t length = 0;
    char *writeStr = strdup(myStr);
    char *outStr = NULL;

    lab3_5(filePath, writeStr, len - 1);
    if((fp = fopen(filePath, "rb")) == NULL){
        printf("Lab3_5 Fail!\nerror opening file\nerrno: %d\n", errno);
        remove(filePath);
        free(writeStr);
	exit(0);
    }
    if((read = getline(&outStr, &length, fp)) == -1){
	printf("Lab3_5 Fail!\nerror reading from file\nerrno: %d\n", errno);
	remove(filePath);
    free(writeStr);
	free(outStr);
	fclose(fp);
	exit(0);
    }
    if(strncmp(outStr, myStr, length) != 0){
	printf("Lab3_5 Fail!\nincorrect string read from file\nreceived: %s\nexpected: %s\n", outStr, myStr);
	remove(filePath);
	free(writeStr);
	free(outStr);
	fclose(fp);
	exit(0);
    }
    printf("Lab3_5 Pass!\n");
    free(writeStr);
    free(outStr);
    fclose(fp);
}

void verifyOpt1() {
    char *testStrs[] = {"Loop", "T0nk4", "TApe Recorder", "y3r 4 h4ck3r h4rRy"};
    char *ansStrs[] = {"LOOP", "T0NK4", "TAPE RECORDER", "Y3R 4 H4CK3R H4RRY"};
    char *src = NULL;
    char *dst = NULL;
    size_t len = 0;
    for(uint i = 0; i < sizeof(testStrs)/sizeof(testStrs[0]); i++){
	len = strlen(testStrs[i]) + 1;
        src = strdup(testStrs[i]);
        dst = calloc(1, len);

        optional_1(dst, src);

        if(strncmp(dst, ansStrs[i], strlen(ansStrs[i]) + 1) != 0){
            printf("Optional_1 Fail!\ncase: %s\ndst: %s\nexpected: %s\n", testStrs[i], dst, ansStrs[i]);
            free(src);
	    free(dst);
	    exit(0);
        }
        free(src);
        free(dst);
    }
    printf("Optional_1 Pass!\n");
}

void verifyOpt2() {
    size_t len = 20;
    char *dst = calloc(1, len);
    optional_2(dst, len);
    free(dst);
    printf("There are no checks for Optional_2. You will segfault if you do it incorrectly\n");
}
