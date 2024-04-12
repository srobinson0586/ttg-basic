#include "shell.h"

#define MAX_CMD 1024

/*
 * To compile and run the program, type:
 * 	$ make
 */

int main() {
	char *cmd_buf = NULL;
	
	help();	
	
	while(1) {
		printf("$ "); // shell prompt

		// TODO: get shell command from user

		// TODO: check for exit command

		// TODO: check for wc cmd_buf

		// TODO: check for cat command

		// TODO: check for student command

		// TODO: check for student print command

		// TODO: check for unrecognized command

		// TODO: free cmd_buf

	}

	// TODO: cleanup before exiting

}
