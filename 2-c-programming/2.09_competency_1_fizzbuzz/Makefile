CC = gcc
CFLAGS = -g -Wall -Wextra

.PHONY: run clean

run: exercise
	valgrind --leak-check=full --show-leak-kinds=all ./exercise

exercise: exercise.c
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f exercise