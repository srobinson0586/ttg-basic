CC = gcc
CFLAGS = -g -Wall -Wextra
target = hash_table

run: $(target)
	valgrind --leak-check=full --show-leak-kinds=all ./$(target)

$(target): $(target).c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	-rm -f $(target)

.PHONY: run clean
