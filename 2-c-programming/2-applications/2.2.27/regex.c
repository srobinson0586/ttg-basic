//compile with gcc -w
#include <stdio.h>
#include <stdlib.h>
#include <regex.h>
const char *string_ex_1 = "this192.168.31.2_is_192.168.313.31example_192.44.22.1of_extracting_192.55.11.1IP_addresses.";
const char* string_ex_2 = "this192.168.31._is_192.313.31example_192..22.1of_extracting_192.55.IP_addresses.";
const char* string_ex_3 = "this192a.168.31.2_is_192.168.z313.31example_192.44.a22.1of_extracting_192.55.11a.1IP_addresses.";
const char* string_ex_4 = "this192a.168.31.2_is_192.168.z313.31example_192.44.a22.1of_extracting_192.55.11a.1IP_addresses0.0.0.0aaaa100.100.10.33kkkssssssssssssssssssssssssssssssss";

/*
Helper function to print result of whether or not a pattern was matched on a call to `regexec`
params:
	int value - 0 means success, REG_NOMATCH defined in regex.h as failure
*/
void print_result(int value)
{
 
    // If pattern found
    if (value == 0) { 
        printf("Pattern found. %d\n", value );
    }
 
    // If pattern not found
    else if (value == REG_NOMATCH) {
        printf("Pattern not found. %d\n", value );
    }
 
    // If error occurred during Pattern
    // matching
    else {
        printf("An error occurred.\n");
    }
}

/*
Helper function to print a substring of `string`
params:
	int start - The index to begin printing at
	int end   - The index to stop printing at
*/
void print_partial_string(const char* string, int start, int end)
{
   printf("\nMatch Found:  ");
   for (; start < end; start++)
   {
      printf("%c", string[start]);
   }
   printf("\n");

}

/*
Devise a regex to match an IPv4 address in the format of X.X.X.X where X is an integer.
Compile the regex where indicted and use the `regexec` function call to detect a match.
*/
void ex_1(const char *input_string)
{

	int return_value = -1;	// used to store return value of regexec() & regcomp() calls
	regex_t regex_obj; 		// for use in regcomp. See regex attachment 1 for details. Do not use any other resource.
	
	/* TODO: Using the above reference,  call regcomp with three args. 
	1st arg: The regex_t object by reference
	2nd arg: The string regex pattern in quotes
	3rd arg: Use REG_EXTENDED enum value
	
	See the markdown "Requirements" 'section for what is considered a valid IPv4 address that you should search for.
	*/
	// ONE LINE HERE; use return_value variable 
	
	if (return_value ==0)
	{
		printf("reg_object compiled.\n");
	}
	else
	{
		printf("Reg_object failed compilation.\n");
		exit(EXIT_FAILURE);
	}

	// TODO: Call regexec, which actually searches the input string, and get the return value.
    // ONE LINE HERE; use return_value variable
	
	print_result (return_value);
	return;
}

/*
Use repeated calls to `regexec` to find all IPv4 address matches and call the `print_partial_string()` function
  to print every IP address found.
*/
void ex_2(const char *input_string)
{
	/*
	In this function you will actually count the number of matches in each string print each match.
	Unfortunately, this is not automatic.  Notice that the regexec args are the following:
		int regexec(const regex_t *preg, const char *string, size_t nmatch, regmatch_t pmatch[], int eflags);

	So, what are the last 3 args for?  The key language is on line 58 of the regex_doc.txt file: "If nmatch is 0 or REG_NOSUB...".
	This paragraph should tell you at least 5 important things to count matches and print the entire matched
	expression and its substrings/capture groups, if any:

	1.  the 3rd arg ("nmatch") sets the maximum number of times a pattern will be matched in the input.
	2.  The 4th arg is an array of a object type ("regmatch_t").
	3.  The size of the array for regmatch_t structures must equal the number of potential nmatches (3rd arg).
	- THIS MATCHES SUBEXPRESSIONS AKA CAPTURE GROUPS-- NOT-- every possible regex match in the data!!!
	4.  If the number of subexpression matches is less than the maxixmum (3rd arg), then each element of the remaining 
		structs in the regmatch_t array is set to -1.  
	5.  Finally, the subexpressions/capture groups can be printed from the originally input string with the start and
		end indicies provided in the returned regmatch_t structs.
	*/
    printf("\n-------------------------------------------------------------------------------\n");
	regex_t regex_obj;
	int return_value = -1; 
	
	// TODO: Same call to regcomp as in ex_1
	// ONE LINE HERE; Use return_value
	
	if (return_value ==0)
	{
		printf("reg_object compiled.\n");
	}
	else
	{
		printf("Reg_object failed compilation\n");
		exit(EXIT_FAILURE);
	}
	
	// TODO: Declare the necessary array of structs for this.  The first element is for the complete
	//  matched regex (not any capture groups)
	//ONE LINE HERE
	
	/*
	because we are searching for the entire expression and are not caring
	about capture groups we only need one struct in the array.
	*/
	size_t nmatch = 1; 
	
	// Each element of the rematch_t struct is a signed integer.  see https://www.gnu.org/software/libc/manual/html_node/Regexp-Subexpressions.html
	
	int match_count = 0;
	/* TODO: Write loop, incrementing match_count and printing each matching regex.
	In order to find matches past the first one you must increment the input_string with pointer math to the
		next char after the previous match and pass that into regexec again.
	To print, use the print_partial_string() function provided above.
	Make sure to print total number of matches found at the end.
	Hint: call regexec first to test if there is a match at all(printed No matched found if false), then enter loop.
	Hint: Use REG_NOTBOL for 5th argument
	*/
	
	// ONE LINE HERE (test if theres a match at all); use return_value

	if (return_value == REG_NOMATCH) //must return if no match
	{
	   printf("\nNo Matches found.\n");
	   return;
	}

	while (return_value ==0)
	{
		// TODO: LOOP CODE HERE
	}

	printf("Number of matches found:  %d\n", match_count);
	printf("-------------------------------------------------------------------------------\n");
	return;
}


/*
Modify your regex to include *capture groups* and print any capture groups found
in the four test strings for the first match found.
*/
void ex_3(const char *input_string)
{
    printf("\n-------------------------------------------------------------------------------\n");
	regex_t regex_obj;
	int return_value = -1;

	/* TODO: Implement capture groups in the regex object compilation for the integer groups in an IP address.
	NOTE:  USE REG_EXTENDED again which allows () use per documentation
		   This compilation string will be different than the calls to regcomp in the previous two funcs
	*/
    //ONE LINE HERE; use return_value
	
	if (return_value ==0)
	{
		printf("reg_object compiled.\n");
	}
	else
	{
		printf("reg_object failed compilation.\n");
		exit(EXIT_FAILURE);
	}
	
	// Remember the first element of the regmatch_t array is for the match info, each subsequent 
	// item is for capture group information. You should have 4 capture groups so size is 5.
	regmatch_t match_array[5];
	
	// setting nmatch value
	size_t nmatch = 5; //same size as above for the array
	
	/* TODO: Call regexec before going into the loop to see if theres a match at all
	   NOTE: You should use 0 for the 5th arg, not REG_NOTBOL as in previous calls
	*/
	// ONE LINE HERE (test if theres a match at all); use return_value

	if (return_value == REG_NOMATCH) //must return if no match
	{
	   printf("\nNo Matches found.\n");
	   return;
	}

	/* TODO: Write loop that sends each capture group start and end index to print_partial_string
	You do not need to call regexec again! This means only the capture groups for the first match
	will be printed. Remember to check for valid indicies!  see https://www.gnu.org/software/libc/manual/html_node/Regexp-Subexpressions.html
	*/
	for (int i= 1; i < 5; i++) // 1st capture group (if it exists) is at 1
	{
		// TODO: LOOP CODE HERE
	}

	printf("-------------------------------------------------------------------------------\n");
	return;
}

/*
For testing purposes, remove the comment `\\` before each function call in main.
There are four defined strings that are passed to each of the 3 functions you will finish.
See the markdown for expected results.
*/
int main()
{
	// TODO: Test your functions
	
	//ex_1(string_ex_1);
	//ex_1(string_ex_2);
	//ex_1(string_ex_3);
	//ex_1(string_ex_4);

	//ex_2(string_ex_1);
	//ex_2(string_ex_2);
	//ex_2(string_ex_3);
	//ex_2(string_ex_4);
	
	//ex_3(string_ex_1);
	//ex_3(string_ex_2);
	//ex_3(string_ex_3);
	//ex_3(string_ex_4);
	return 0;
}
