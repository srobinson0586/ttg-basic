CC = gcc
CFLAGS = -g -Wall -Wextra

run: main
	valgrind ./main

main: main.c exercise.o
	$(CC) $(CFLAGS) $^ -o $@

exercise.o: hidden/exercise.c
	$(CC) $(CFLAGS) -c $^ -o $@

clean:
	rm -f main *.o

.PHONY: run clean
