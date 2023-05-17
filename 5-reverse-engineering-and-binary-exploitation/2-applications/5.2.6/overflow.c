#include <stdio.h>
#include <string.h>

// Compile with `gcc -Wall -Wextra -g overflow.c -o overflow`

void vulnFunc(char *arg) {
    char buf[10] = { 0 };
    strcpy(buf, arg);
    printf("Copied argument %s\n", arg);
}

int main(int argc, char *argv[]) {
    vulnFunc(argv[1]);
    return 0;
}
