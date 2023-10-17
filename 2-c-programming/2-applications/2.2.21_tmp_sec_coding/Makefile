CC = gcc
CFLAGS = -g -Wall -Wextra

target = secure_coding

$(target): $(target).c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	-rm -f $(target)

.PHONY: clean
