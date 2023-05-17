#ifdef __unix__

#include <stdlib.h>
#include <stdio.h>

#elif defined(_WIN32) || defined(WIN32)

#include <windows.h>
#include <stdio.h>

#endif

int main() {
	char *str = "hello";
	int x = 65;
	int y = -1;
	float z = 3.141592;

	// TODO: print x as a signed decimal
	// TODO: print x as an unsigned decimal
	// TODO: print x as a hexadecimal
	// TODO: print x as a char

	// TODO: print y as a signed decimal
	// TODO: print y as an unsigned decimal
	// TODO: print y as a hexadecimal

	// TODO: print z as a float with no precision (ie 3.141592)
	// TODO: print z as a float with a precision of 2 (ie 3.14)
	// TODO: print z as a float with a precision of 4 (ie 3.1415)

	// TODO: print str as a string
	// TODO: print str as an address

	return 0;
}
