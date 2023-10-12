CC = gcc
CFLAGS = -g -Wall -Wextra

run: main
	valgrind --leak-check=full --show-leak-kinds=all ./main

main: main.c exercise.o
	$(CC) $(CFLAGS) $^ -o $@

exercise.o: exercise.c
	$(CC) $(CFLAGS) -c $^ -o $@

clean:
	rm -f *.o main

.PHONY: run clean
