executables = mutex semaphore

all: $(executables)

$(executables): %: %.c
	gcc -g -Wall -Wextra -pthread $^ -o $@

clean:
	rm -f $(executables)

.PHONY: all clean
