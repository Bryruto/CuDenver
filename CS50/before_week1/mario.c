#include <stdio.h>
#include <cs50.h>

void print_row(int bricks);

int main(void)
{
    int height;
    // prompt user for input
    do
    {
    height = get_int("what is the height of the pyramid? ");
    }
    while (height <1 || height > 9);

int new = height;
    // print a pyramid of the height
    for (int i =0;i<height;i++)
    {
        for(int q = new - 1;q > 0;q--)
        {
            printf(" ");
        }
        new--;
    print_row(i + 1);
    }
}

void print_row(int bricks)
{
    for(int i=0;i<bricks;i++)
    {
    printf("#");
    }
    printf("\n");
}
