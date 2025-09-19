#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height = 0;

    // Prompt user for a height between 1 and 8 (inclusive)
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    int space = height;

    // Loop through each row
    for (int i = 1; i <= height; i++)
    {
        // Print leading spaces (left pyramid alignment)
        for (int x = 1; x < space; x++)
        {
            printf(" ");
        }

        // Print left-side hashes
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }

        // Print gap between pyramids
        printf("  ");

        // Print right-side hashes
        for (int p = 0; p < i; p++)
        {
            printf("#");
        }

        // Move to the next line
        printf("\n");

        // Reduce leading space count
        space--;
    }
}

