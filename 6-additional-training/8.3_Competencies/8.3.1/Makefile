CC = gcc
CFLAGS = -g -Wall -Wextra

VGFLAGS = --leak-check=full --show-leak-kinds=all --track-origins=yes \
          --suppressions=valgrind_libcrypto_suppressions.txt

target = ssl_client

run: $(target)
	valgrind $(VGFLAGS) ./$(target)

$(target): $(target).c
	$(CC) $(CFLAGS) $^ -o $@ -lssl -lcrypto

clean:
	-rm -f $(target)

.PHONY: run clean
