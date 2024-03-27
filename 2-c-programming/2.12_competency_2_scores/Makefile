CC = gcc
CFLAGS = -g -Wall -Wextra
LIBS = cs50.c

.PHONY: run clean

run: scores
	valgrind --leak-check=full --show-leak-kinds=all ./scores

scores: scores.c $(LIBS)
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f scores