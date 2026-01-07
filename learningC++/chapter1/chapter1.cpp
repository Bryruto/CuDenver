#include <cstdio>

int part1(int x){
    if(x < 0){
        x = x * -1;
    }
    return(x);
}

int sum(int x, int y){
    return(x+y);
}
int main()
{
    int try1 = part1(-987);
    int try2 = part1(3);
    int try3 = part1(20);
    int try4 = part1(-5);
    printf("try1-> %d \ntry2-> %d \ntry3-> %d \ntry4-> %d\n",try1,try2,try3,try4);
    int sum1 = sum(3,3);
    int sum2 = sum(40,3);
    int sum3 = sum(-53,46);
    printf("sum1=%d\nsum2=%d\nsum3=%d",sum1,sum2,sum3);
}