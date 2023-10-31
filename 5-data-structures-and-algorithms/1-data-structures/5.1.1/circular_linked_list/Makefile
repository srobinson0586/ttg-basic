CC = gcc
CFLAGS = -g -Wall -Wextra
target = circular_linked_list

run: $(target)
	valgrind --leak-check=full --show-leak-kinds=all ./$(target)

$(target): $(target).c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	-rm -f $(target)

.PHONY: run clean
