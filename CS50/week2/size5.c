#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // declare an array
    int size[5];
    size[0] = 1;
    // populate the array
    for (int i = 0; i < 4; i++)
    {
        size[i + 1] = size[i] * 2;
    }
    // print out the values one by one
    for (int j = 0; j < 5; j++)
    {
        printf("%i\n", size[j]);
    }
}
