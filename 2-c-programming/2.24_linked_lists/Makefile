CC = gcc
CFLAGS = -g -Wall -Wextra

.PHONY: run clean

run: application
	valgrind --leak-check=full --show-leak-kinds=all ./application

application: application.c
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f application