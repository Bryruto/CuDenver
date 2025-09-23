#include <cs50.h>
#include <stdio.h>

void draw(int size);

int main(void)
{
    int size = get_int("size ");
    draw(size);
}
void draw(int size)
{
        for (int i=0;i<size;i++)
    {
        for (int x=0;x<i+1;x++)
        {
            printf("#");
        }
        printf("\n");
    }
}
