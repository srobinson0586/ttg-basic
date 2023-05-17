CC = gcc
CFLAGS = -g -Wall -Wextra

products = client server

requirements = lpp.o utils.o

all: $(products)

$(products): %: %.c $(requirements)
	$(CC) $(CFLAGS) $^ -o $@

lpp.o: lpp.c
	$(CC) $(CFLAGS) -c $^ -o $@

utils.o: utils.c
	$(CC) $(CFLAGS) -c $^ -o $@

clean:
	rm -f *.o $(products) *~

.PHONY: all clean
