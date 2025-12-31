#include <cstdio>

int part1(int x){
    if(x < 0){
        x = x * 1;
    }
    return(x);
}

int main()
{
    int try1 = part1(-987);
    int try2 = part1(3);
    int try3 = part1(20);
    int try4 = part1(-5);
    printf("try1-> %d \ntry2-> %d \ntry3-> %d \ntry4-> %d",try1,try2,try3,try4);
    return 0;
}