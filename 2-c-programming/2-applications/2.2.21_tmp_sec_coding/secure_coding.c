#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// TODO: print 5 addresses from the stack
void format_string_vuln(char* attack){
	return;
}


// TODO: remove instances of '-' from the string
void input_sanitization(char* str){
	return;
}

// TODO: Securely zero out num_bytes number of bytes at the memory address pointed at by ptr
void zero_memory(void* ptr, int num_bytes) {
	return;
}


int main(int argc, char** argv) {
	int mem_len = 512;
	//Determine what string is needed to print 5 addresses from the stack
	if (argc == 1) {
		printf("Enter an argument to be passed to format_string_vuln.\n\n");
	} else {
		format_string_vuln(argv[1]);
	}

	//Testing for input_sanitization
	char test[] = "-Hello - World";
	printf("Before: %s\n", test);
	input_sanitization(test);
	printf("After: %s\n", test);
	if(strcmp(test, "Hello  World") != 0){
		printf("Input is not sanitized\n");
		exit(0);
	}
	printf("Passed Input Sanitization!\n\n");


	// Testing memory clearing
	printf("Testing Memory Clearing . . .\n");
	void* ptr = malloc(mem_len);
	strcpy((char*)ptr, "hello");
	zero_memory(ptr, mem_len);
	for(int i = 0; i < mem_len; i++){
		if(((char*)ptr)[i] != 0){
			printf("Memory is not cleared\n");
			exit(0);
		}
	}
	free(ptr);
	printf("Passed Memory Clearing!\n");
	
	return 0;
}
