executables = mutex semaphore conditionals threadpool

all: $(executables)

$(executables): %: %.c
	gcc -g -Wall -Wextra -pthread $^ -o $@

clean:
	rm -f $(executables)

.PHONY: all clean
