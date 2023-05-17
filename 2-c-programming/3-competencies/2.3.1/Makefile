CC = gcc
CFLAGS = -g -Wall -Wextra

run: main
	valgrind ./main

main: main.c exercise.o
	$(CC) $(CFLAGS) $^ -o $@

exercise.o: exercise.c
	$(CC) $(CFLAGS) -c $^ -o $@

clean:
	rm -f *.o main

.PHONY: run clean
