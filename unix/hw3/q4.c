#include <stdio.h>
#include <sys/stat.h>
#include <dirent.h>
#include <unistd.h>
#include <errno.h>

#define DIR_PERM 0777

// this will test the directory 
void test_dir(const char *path)
{
    DIR *dir = opendir(path);

    if (dir == NULL) {
        printf("%s: FAILED, errno = %d\n", path, errno);
    }
    else {
        printf("%s: SUCCEEDED\n", path);

        if (closedir(dir) == -1) {
            perror("closedir failed");
        }
    }
}

int main(int argc, char *argv[])
{
    // check that we have a path 
    if (argc != 2 || argv[1][0] != '/') {
        printf("Usage: %s <directory path>\n", argv[0]);
        return 1;
    }

    const char *DIR_NAME = argv[1];

    // make a directory 
    if (mkdir(DIR_NAME, DIR_PERM) == -1) {
        perror("mkdir failed");
        return 1;
    }

    // enter the directory to change current working 
    if (chdir(DIR_NAME) == -1) {
        perror("chdir failed");
        return 1;
    }

    // remove the directory 
    if (rmdir(DIR_NAME) == -1) {
        perror("rmdir failed");
        return 1;
    }

    printf("rmdir succeeded!\n");

    //then run test make sure it all worked right 
    test_dir(".");
    test_dir("../hw3");
    test_dir(DIR_NAME);

    return 0;
}
