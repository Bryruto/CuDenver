#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>

int my_dup2_with_fcntl(int old, int new)
{
    //check the old one
    if (fcntl(old, F_GETFD) == -1) {
	return -1;
    }

    // make sure new one is valid
    if (new < 0) {
	errno = EBADF;
        return -1;
    }

    // If old and new are the same
    if (old == new) {
        return new;
    }

    // close new if already open
    close(new);

	
    return fcntl(old, F_DUPFD, new);
}

int main(int argc, char **argv) {
    if (argc != 3) {
	printf("Usage: %s <new_fd> <filename>\n", argv[0]);
	return 1;
    }

    int newfd = atoi(argv[1]);

    // need to open the file
    int oldfd = open(argv[2], O_RDWR | O_CREAT, 0644);

    if (oldfd == -1) {
        perror("open");
        return 1;
    }

    // test the function for errors 
    int result = my_dup2_with_fcntl(oldfd, newfd);

    if (result == -1) {
        perror("my_dup2_with_fcntl");
        close(oldfd);
        return 1;
    }

    printf("- old fd : %d\n", oldfd);
    printf("- new duped fd: %d\n", result);

    // use the read linkfunction
    char path[100];
    char filename[100];
    ssize_t len;

    // get the old path
    snprintf(path, sizeof(path), "/proc/self/fd/%d", oldfd);
    len = readlink(path, filename, sizeof(filename) - 1);

    if (len != -1) {
        filename[len] = '\0';
        printf("- %s: old fd path: %s\n", path, filename);
    } else {
        perror("readlink oldfd");
    }

    // get the new path
    snprintf(path, sizeof(path), "/proc/self/fd/%d", result);
    len = readlink(path, filename, sizeof(filename) - 1);

    if (len != -1) {
        filename[len] = '\0';
        printf("- %s: new fd path: %s\n", path, filename);
    } else {
        perror("readlink newfd");
    }

    if (result != oldfd)
        close(result);

    close(oldfd);

    return 0;
}
