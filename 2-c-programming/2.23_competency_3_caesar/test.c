#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FILENAME_LENGTH 256

// Function prototypes
void testEncryptionDecryption(char *inputFileName, char *outputFileName, int key);

int main() {
    char inputFileName[MAX_FILENAME_LENGTH] = "test.txt";
    char encryptedFileName[MAX_FILENAME_LENGTH] = "encrypted.txt";
    char decryptedFileName[MAX_FILENAME_LENGTH] = "decrypted.txt";
    int key = 5;

    // Test encryption and decryption
    testEncryptionDecryption(inputFileName, encryptedFileName, key);
    testEncryptionDecryption(encryptedFileName, decryptedFileName, -key);

    return 0;
}

void testEncryptionDecryption(char *inputFileName, char *outputFileName, int key) {
    FILE *inputFile, *outputFile;
    char buffer[1024];
    
    // Open input file for reading
    inputFile = fopen(inputFileName, "r");
    if (inputFile == NULL) {
        printf("Error: Unable to open input file %s\n", inputFileName);
        exit(1);
    }

    // Open output file for writing
    outputFile = fopen(outputFileName, "w");
    if (outputFile == NULL) {
        printf("Error: Unable to open output file %s\n", outputFileName);
        fclose(inputFile);
        exit(1);
    }

    // Process input file and write output file
    while (fgets(buffer, sizeof(buffer), inputFile) != NULL) {
        // Encrypt or decrypt line
        for (int i = 0; i < strlen(buffer); i++) {
            buffer[i] += key;
        }
        // Write to output file
        fputs(buffer, outputFile);
    }

    // Close files
    fclose(inputFile);
    fclose(outputFile);

    printf("File %s processed successfully.\n", inputFileName);
}
