CC = gcc
CFLAGS = -g -Wall -Wextra

test: student_getline.c harness.c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	rm -f *.o test rand.txt *~

.PHONY:	clean
