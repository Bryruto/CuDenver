#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int cents;

    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    int times = 0;

    while (cents > 0)
    {
        if (cents >= 25)
        {
            cents -= 25;
            times++;
        }
        else if (cents >= 10)
        {
            cents -= 10;
            times++;
        }
        else if (cents >= 5)
        {
            cents -= 5;
            times++;
        }
        else
        {
            cents--;
            times++;
        }
    }

    printf("%i\n", times);
}
