CC = gcc
CFLAGS = -g -Wall -Wextra
LIBS = cs50.c

.PHONY: run clean

run: exercise
	valgrind --leak-check=full --show-leak-kinds=all ./exercise

exercise: exercise.c $(LIBS)
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f exercise
