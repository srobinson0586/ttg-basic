CC = gcc
CFLAGS = -g -Wall -Wextra

# We need to use the '-no-pie' option with gcc. For some reason, gcc
# refuses to use the PLT for external calls from the assembly code
# unless you pass it -no-pie.
test: test.o linked_list.o
	$(CC) $(CFLAGS) -no-pie $^ -o $@

test.o: test.c
	$(CC) $(CFLAGS) -c $^ -o $@

linked_list.o: linked_list.asm
	nasm -f elf64 -g -F dwarf $^ -o $@

.PHONY: clean

clean:
	rm -f test *.o *~
