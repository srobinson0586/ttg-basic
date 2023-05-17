#include <stdio.h>
#include <stdlib.h>

int sum(int a, int b, int c) {
    int x = a + b;
    int y = c;

    return x + y;
}

int main() {
    
    int my_sum = 0;
    my_sum = sum(0xAA, 0xBB, 0xCC);
    return 0;

}
