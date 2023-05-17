CC = gcc
CFLAGS = -g -Wall -Wextra

target = binary_search_tree

run: $(target)
	valgrind ./$(target)

$(target): $(target).c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	-rm -f $(target)

.PHONY: run clean
