#include <stdio.h>
#include <string.h>

int main(){

    char originalString[] = "It would be very annoying to count the characters in this strings so just find it out programatically."
    int stringSize;
    char *wordArray;
    //TODO: Store the character count of sampleSting in stringSize

    //TODO: Split the functions on spaces and store an array. Store result in wordArray.
    //HINT: Look up how to use strtok.

    char newString[stringSize];
    //TODO: Use a for loop to concatanate all values adding back the spaces into one string. Store in newString.

    bool cmpResult;
    //TODO: Compare newString and originalString and make sure they are equal using strcmp(). Store result in cmpResult

    if(cmpResult != 0){
        printf("The strings are not equal");
        return 1;
    }
    
    printf("The strings are equal!");
    return 0;
}