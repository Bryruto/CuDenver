#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height = 0;

    // Prompt user for a valid height between 1 and 8
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // Print pyramid rows
    for (int i = 1; i <= height; i++)
    {
        // Print leading spaces
        for (int x = 0; x < height - i; x++)
        {
            printf(" ");
        }

        // Print hashes
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }

        // Move to the next line
        printf("\n");
    }
}
