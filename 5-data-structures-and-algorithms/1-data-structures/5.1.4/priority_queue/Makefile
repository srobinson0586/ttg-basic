CC = gcc
CFLAGS = -g -Wall -Wextra
target = priority_queue

run: $(target)
	valgrind --leak-check=full --show-leak-kinds=all ./$(target)

$(target): $(target).c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	-rm -f $(target)

.PHONY: run clean
