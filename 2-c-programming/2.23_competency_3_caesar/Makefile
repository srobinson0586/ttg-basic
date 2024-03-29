CC = gcc
CFLAGS = -g -Wall -Wextra

.PHONY: run clean

run: caesar
	valgrind --leak-check=full --show-leak-kinds=all ./caesar

application: caesar.c
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f caesar
