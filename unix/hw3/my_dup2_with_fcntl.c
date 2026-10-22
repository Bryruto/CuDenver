 
#include <unisted.h>
#include <fcntl.h>
#include <errno.h>

int my_dup2_with_fcntl(int old, int newfd){

        //check if old is valid
        if(fcntl(old,F_GETFD)== -1 ){
                return -1;
        }

        //if both old and new are the same
        if (old == new){
                return new;
        }

        //close new if open
        close(new);


        //duplicate old into new
        return fcntl(oldm F_DUPFD, newfd);
}
