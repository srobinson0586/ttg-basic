#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>


typedef struct _data {
	int size;
	int short_num;
	int info;
}data;

typedef struct _smaller_data {
	int size;
	int short_num;
}smaller_data;


/*
*  	Reads in data from the FILE stream to the a buffer to be interpreted as its data structure. Must read in the correct number of
*	bytes for each type of structure. Data is stored in big endian.
* 	params: 
*			void** data_buf - the buffer to read the data into
*			FILE* f 		- the file stream to read the data in from
*	returns:
*			void
*/
void read_data(void** data_buf, FILE* f) {
}


/*
*  	Write data buffer to the FILE stream. Must write the correct number of bytes for each type of structure. 
*	Store data in big endian.
* 	params: 
*			void* data_buf  - the buffer to store
*			FILE* f 		- the file stream to write the data to
*	returns:
*			void
*/
void write_data(void* data_buf, FILE* f) {
	return;
}


/*
* Main is provied to you so you can test your implementation of the serialization.
*/
int main() {
	void* data_buf;
	data *d = calloc(sizeof(data), 1);
	d->size = sizeof(data);
	d->short_num = 12;
	d->info = 1234;

	smaller_data *s_d = calloc(sizeof(smaller_data), 1);
	s_d->size = sizeof(smaller_data);
	s_d->short_num = 34;

	// First, write the data to the file using the student's methods.
	FILE* f = fopen("data", "w+b");

	write_data(d, f);
	write_data(s_d, f);

	free(d);
	free(s_d);
	fclose(f);

	// Now read the data back from the file and verify it's the same.
	f = fopen("data", "rb");

	// First check the struct `data`.
	read_data(&data_buf, f);
	data *read_d = (data*) data_buf;

	if (ntohl(read_d->size) != 12 ||
		ntohl(read_d->short_num) != 12 ||
		ntohl(read_d->info) != 1234) {
		printf("Data deserialized incorrectly.\n");
	} else {
		printf("Successfully deserialized data\n");
	}
	
	free(data_buf);
	data_buf = NULL;

	// Now test the struct `smaller_data`.
	
	read_data(&data_buf, f);
	smaller_data *read_s_d = (smaller_data*) data_buf; 

	if (ntohl(read_s_d->size) != 8 ||
	   ntohl(read_s_d->short_num) != 34) {
		printf("Smaller Data deserialized incorrectly.\n");
	} else {
		printf("Successfully deserialized smaller data\n");
	}
	free(data_buf);

	fclose(f);
	return 0;
}
