CC = gcc
CFLAGS = -g -Wall -Wextra

run: main
	valgrind --leak-check=full ./main

main: shell.o main.c
	$(CC) $(CFLAGS) $^ -o $@

shell.o: shell.c shell.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f *.o main

.PHONY: run clean
