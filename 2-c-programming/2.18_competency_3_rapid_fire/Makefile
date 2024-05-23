CC = gcc
CFLAGS = -g -Wall -Wextra

run: main
	valgrind --leak-check=full --show-leak-kinds=all ./main

main: main.c exercise.o
	$(CC) $(CFLAGS) $^ -o $@ -lm

exercise.o: exercise.c
	$(CC) $(CFLAGS) -c $^ -o $@ -lm

clean:
	rm -f *.o main

.PHONY: run clean
