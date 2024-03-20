run: competency
	valgrind ./competency

# We need --no-pie to allow the relocation for `strncpy`
# in the assembly file.
competency: competency.o main.c
	gcc -g -Wall -Wextra -no-pie $^ -o $@

competency.o: competency.asm
	nasm -f elf64 -g -F dwarf $^ -o $@

clean:
	rm -f *.o competency test.txt

.PHONY: run clean
