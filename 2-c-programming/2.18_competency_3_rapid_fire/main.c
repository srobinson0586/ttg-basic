#include "exercise.h"

#define SIZE 7
#define SIZE_PRIME 100

/*
 * compile and run:
 *     $ make
 */

void SectionOne();
void SectionTwo();
void SectionThree();
void SectionFour();
void SectionFive();

void failCase(char *testFunc, char *failCase);
void passCase(char *testFunc);

int main() {
    // Section 1 - basics
    SectionOne();

    // Section 2 - math
    SectionTwo();

    // Section 3 - control flow
    SectionThree();

    // Section 4 - pointers
    SectionFour();

    // Section 5 - file i/o
    SectionFive();

    printf("Congrats! You have successfully completed the C Verifier\n");
    return 0;
}

void SectionOne() {
    printf("\n---B451C5---\n");
    // TODO: implement SectionOneOne
    SectionOneOne();

    // TODO: implement SectionOneTwo
    SectionOneTwo(0, "the way to get started is to quit talking and begin doing");
    SectionOneTwo(1, "carpe diem");
    SectionOneTwo(2, "there\'s no crying in c0d1ng");
}

void SectionTwo() {
    printf("\n---M47H---\n");
    int x = 1337;
    // TODO: implement SectionTwoOne
    if(SectionTwoOne(x) != x + 1) {
        failCase("SectionTwoOne", NULL);
        exit(0);
    }
    passCase("SectionTwoOne");

    // TODO: implement SectionTwoTwo
    x = 5;
    int y = 6;
    if(SectionTwoTwo(x, y) != 15625) {
        failCase("SectionTwoTwo", NULL);
        exit(0);
    }
    passCase("SectionTwoTwo");

    // TODO: implement SectionTwoThree
    x = 45;
    y = 26;
    if(SectionTwoThree(x, y) != 19) {
        failCase("SectionTwoThree", NULL);
        exit(0);
    }
    passCase("SectionTwoThree");

    x = 1;
    if(SectionTwoFour(x) != x - 1){
        failCase("SectionTwoFour", NULL);
        exit(0);
    }
    passCase("SectionTwoFour");

    x = 7;
    y = 3;
    if(SectionTwoFive(x, y) != 2) {
        failCase("SectionTwoFive", NULL);
        exit(0);
    }
    passCase("SectionTwoFive");

}

void SectionThree() {
    printf("\n---C0N7R0L_FL0W---\n");
    // TODO: implement SectionThreeOne
    int nums[SIZE] = {0, 4, 7, 65, 87, -15, 45};
    if(SectionThreeOne(nums, SIZE) != 193) {
        failCase("SectionThreeOne", NULL);
        exit(0);
    }
    passCase("SectionThreeOne");

    // TODO: implement SectionThreeTwo
    if(SectionThreeTwo(nums, SIZE) != 208) {
        failCase("SectionThreeTwo", NULL);
        exit(0);
    }
    passCase("SectionThreeTwo");

    // TODO: implement SectionThreeThree
    for(int i = 0; i < SIZE; i++) {
        if(SectionThreeThree(nums, SIZE, i) != nums[i]) {
            failCase("SectionThreeThree", NULL);
            exit(0);
        }
    }

    if(SectionThreeThree(nums, SIZE, -12) != -1) {
        failCase("SectionThreeThree", "negative index");
        exit(0);
    }

    if(SectionThreeThree(nums, SIZE, 15) != -1) {
        failCase("SectionThreeThree", "index greater than size of array");
        exit(0);
    }

    if(SectionThreeThree(nums, SIZE, SIZE) != -1) {
        failCase("SectionThreeThree", "index equal to size of array");
        exit(0);
    }

    passCase("SectionThreeThree");

    // TODO: Implement SectionThreeFour
    int nums_prime[SIZE_PRIME];
    int prime_set[25] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
    for(int i = 0; i < SIZE_PRIME; i++) {
        nums_prime[i] = i+1;
        int skip_loop = 0;
        for(int j = 0; j < 25; j++) {
            if(prime_set[j] == nums_prime[i]) {
                if(SectionThreeFour(nums_prime[i]) != 1) {
                    char *tmp_str = calloc(15, 1);
                    snprintf(tmp_str, 15, "%d is prime", prime_set[j]);
                    failCase("SectionThreeFour", tmp_str);
                    free(tmp_str);
                    exit(0);
                }
                skip_loop = 1;
                break;
            }
        }
        if(skip_loop == 1) continue;
        if(SectionThreeFour(nums_prime[i]) != 0) {
            char *tmp_str = calloc(20, 1);
            snprintf(tmp_str, 20, "%d is not prime", nums_prime[i]);
            failCase("SectionThreeFour", tmp_str);
            free(tmp_str);
            exit(0);
        }
    }

    if(SectionThreeFour(-12) != 0) {
        failCase("SectionThreeFour", "negative numbers are not prime");
        exit(0);
    }
    if(SectionThreeFour(0) != 0) {
        failCase("SectionThreeFour", "zero is not prime");
        exit(0);
    }
    passCase("SectionThreeFour");

    int **twoDArray = malloc(sizeof(int*) * 2);
    for(int x = 0; x < 2; x++){
        twoDArray[x] = malloc(sizeof(int) * 2);
    }
    twoDArray[0][0] = 1;
    twoDArray[0][1] = 2;
    twoDArray[1][0] = 3;
    twoDArray[1][1] = 4;
    if(SectionThreeFive(twoDArray, 2, 2) != 10){
        failCase("SectionThreeFive", "did not sum correctly");
        exit(0);
    }
    for(int y = 0; y < 2; y++){
        free(twoDArray[y]);
    }
    free(twoDArray);

    passCase("SectionThreeFive");

    if(SectionThreeSix(1) != 1){
        failCase("SectionThreeSix", "did not match correctly");
        exit(0);
    }
    if(SectionThreeSix(3) != 3){
        failCase("SectionThreeSix", "did not match correctly");
        exit(0);
    }
    if(SectionThreeSix(2) != 2){
        failCase("SectionThreeSix", "did not match correctly");
        exit(0);
    }
    passCase("SectionThreeSix");
}

void SectionFour() {
    printf("\n---P01N73RZ---\n");
    char *good_str = "p01n73rz";
    char *bad_str = "b4d_b01z";
    char *other = "AAAAAAAAAAAAAAAAAAAAAA";

    if(SectionFourOne(good_str) != 1) {
        failCase("SectionFourOne", good_str);
        exit(0);
    }
    if(SectionFourOne(bad_str) != 0) {
        failCase("SectionFourOne", bad_str);
        exit(0);
    }
    if(SectionFourOne(other) != 0) {
        failCase("SectionFourOne", other);
        exit(0);
    }
    passCase("SectionFourOne");

    // TODO: implement SectionFourTwo
    char *almost_good_str = "p01nt3Rz";
    if(SectionFourTwo(good_str, strlen(good_str)) != 1) {
        failCase("SectionFourTwo", good_str);
        exit(0);
    }
    if(SectionFourTwo(bad_str, strlen(bad_str)) != 0) {
        failCase("SectionFourTwo", bad_str);
        exit(0);
    }
    if(SectionFourTwo(almost_good_str, 4) != 1) {
        failCase("SectionFourTwo", almost_good_str);
        exit(0);
    }
    if(SectionFourTwo(almost_good_str, strlen(almost_good_str)) != 0) {
        failCase("SectionFourTwo", almost_good_str);
        exit(0);
    }

    passCase("SectionFourTwo");

    // TODO: implement SectionFourThree
    char *dst_good = calloc(strlen(good_str)+1, 1);
    char *dst_bad = calloc(strlen(bad_str)+1, 1);
    char *dst_other = calloc(strlen(other)+1, 1);

    SectionFourThree(&dst_good, good_str);
    if(strcmp(dst_good, good_str) != 0) {
        failCase("SectionFourThree", good_str);
        goto _exit;
    }

    SectionFourThree(&dst_bad, bad_str);
    if(strcmp(dst_bad, bad_str) != 0) {
        failCase("SectionFourThree", bad_str);
        goto _exit;
    }

    SectionFourThree(&dst_other, other);
    if(strcmp(dst_other, other) != 0) {
        failCase("SectionFourThree", other);
        goto _exit;
    }

    passCase("SectionFourThree");

    // TODO: implement SectionFourFour
    int x = 10, y = 25, tmp_x = x, tmp_y = y;
    SectionFourFour(&x, &y);
    if(x != tmp_x * 5 && y != tmp_y * 5) {
        failCase("SectionFourFour", NULL);
        goto _exit;
    }

    goto _pass;

 _exit:
    free(dst_good);
    free(dst_bad);
    free(dst_other);
    exit(0);
 _pass:
    free(dst_good);
    free(dst_bad);
    free(dst_other);
    passCase("SectionFourFour");

    // TODO: implement SectionFourFive
    SectionFourFive();
    printf("i have no way to verify that you did SectionFourFive, but i trust you...\n");
    passCase("SectionFourFive");

    // TODO: implement SectionFourSix
    char a1[4] = {0xff, 0xff, 0xff, 0xff};
    char a2[4] = {0x78, 0x56, 0x34, 0x12};
    char a3[4] = {0x00, 0x00, 0x00, 0x00};
    if(SectionFourSix(a1) != 0) {
        failCase("SectionFourSix", NULL);
        exit(0);
    }
    if(SectionFourSix(a2) != 0x12345679) {
        failCase("SectionFourSix", NULL);
        exit(0);
    }
    if(SectionFourSix(a3) != 1) {
        failCase("SectionFourSix", NULL);
        exit(0);
    }
    passCase("SectionFourSix");

}

void SectionFive() {
    printf("\n---F1L3_1/0---\n");
    // TODO: implement SectionFiveOne
    char* file_name = "7r010101.txt";
    char* tmp_str = "hello creul world\n";
    if(SectionFiveOne(file_name, tmp_str) != 0) {
        failCase("SectionFiveOne", "why error writing/creating file?");
        goto _exit;
    }
    passCase("SectionFiveOne");

    // TODO: implement SectionFiveTwo
    if(SectionFiveTwo(file_name) == -1) {
        failCase("SectionFiveTwo", "why error getting file size?");
        goto _exit;
    }

    if(SectionFiveTwo(file_name) != (ssize_t) strlen(tmp_str)) {
        printf("size = %ld\n", strlen(tmp_str));
        failCase("SectionFiveTwo", "size of file doesn\'t match size of buffer");
        goto _exit;
    }
    passCase("SectionFiveTwo");

    // TODO:implement SectionFiveThree
    char *read_str = NULL;
    if(SectionFiveThree(file_name, &read_str) == -1) {
        failCase("SectionFiveThree", "error getting file contents");
        free(read_str);
        goto _exit;
    }
    free(read_str);

    if(SectionFiveThree(file_name, &read_str) != (ssize_t) strlen(tmp_str) + 1) {
        failCase("SectionFiveThree", "number of bytes read doesn\'t match size of buffer");
        free(read_str);
        goto _exit;
    }
    free(read_str);

    SectionFiveThree(file_name, &read_str);
    if(strncmp(read_str, tmp_str, strlen(read_str) + 1) != 0) {
        failCase("SectionFiveThree", "incorrect buffer read");
        free(read_str);
        goto _exit;
    }
    free(read_str);
    passCase("SectionFiveThree");
    if(remove(file_name) != 0) {
        printf("could not delete %s\n", file_name);
    }

    read_str = "test";
    file_name = "test.txt";
    if(SectionFiveFour(file_name, read_str) != 8) {
        failCase("SectionFiveFour", "incorrect file size");
        goto _exit;
    }
    // Make sure they deleted the file.
    if (fopen(file_name, "r")) {
        failCase("SectionFiveFour", "failed to delete the file");
        goto _exit;
    }
    passCase("SectionFiveFour");

    return;

 _exit:
    exit(0);
}

void failCase(char *testFunc, char *failCase) {
    printf("%s: FAIL!\n", testFunc);
    if(failCase == NULL) return;
    printf("\tFAIL: %s\n", failCase);
}

void passCase(char *testFunc) {
    printf("%s: PASS!\n", testFunc);
}
