CC = gcc
CFLAGS = -g -Wall -Wextra
LIBS = cs50.c

.PHONY: run clean

run: fizzbuzz
	valgrind --leak-check=full --show-leak-kinds=all ./fizzbuzz

fizzbuzz: fizzbuzz.c $(LIBS)
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f fizzbuzz
