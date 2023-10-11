CC = gcc
CFLAGS = -g -Wall -Wextra

target = weighted_graph

run: $(target)
	valgrind ./$(target)

$(target): $(target).c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	-rm -f $(target)

.PHONY: run clean
