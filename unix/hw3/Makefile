CC = gcc
CFLAGS = -Wall -Wextra -g
TARGETS = my_dup2_test q4

all: $(TARGETS)

my_dup2_test: my_dup2_with_fcntl.c
	$(CC) $(CFLAGS) -o my_dup2_test my_dup2_with_fcntl.c

q4: q4.c
	$(CC) $(CFLAGS) -o q4 q4.c

clean:
	rm -f $(TARGETS)
