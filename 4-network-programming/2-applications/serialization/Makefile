CC = gcc
CFLAGS = -g -Wall -Wextra

target = serialization

run: $(target)
	valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./$(target)

$(target): $(target).c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	-rm -f $(target)

.PHONY: run clean
