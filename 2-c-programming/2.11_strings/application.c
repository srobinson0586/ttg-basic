#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main(){

    char originalString[] = "It would be very annoying to count the characters in this strings so just find it out programatically.";
    int stringSize;
    char *wordArray[18];
    //TODO: Store the character count of sampleSting in stringSize

    //TODO: Create a character buffer called copiedString that has enough space for 128 characters. Store a copy of originalString in copiedString.

    //TODO: Split the copiedString on spaces and store each word in wordArray
        //HINT: Look up how to use strtok.

    char newString[stringSize];
    //TODO: Use a for loop to concatanate all values in wordArray (adding back the spaces) into one string. Store in newString.

    bool cmpResult;
    //TODO: Compare newString and originalString and make sure they are equal using strcmp(). Store result in cmpResult

    if(cmpResult != 0){
        printf("The strings are not equal");
        return 1;
    }
    
    printf("The strings are equal!");
    return 0;
}