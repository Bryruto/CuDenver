#include <cs50.h>
#include <stdio.h>

void draw(int n);

int main(void)
{
    int size =get_int("size: ");
    draw(size);
}

void draw(int n)// n is what is getting passed through
{
    if (n<=0)
    {
        return;
    }

    draw(n-1);// call it self

    for (int i =0;i<n;i++)//print form 1 then new line then call ifself again and again till i<0 is false
    {
        printf("#");
    }
    printf("\n");
}
