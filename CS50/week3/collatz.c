#include <cs50.h>
#include <string.h>
#include <stdio.h>

int collatz(int number);

int main(void)
{
int number =get_int("number: ");
int time = collatz(number);
}

int collatz(int number)
{
    if(number == 1)
    {
        return 0;
    }
    else if ((number % 2) == 0)
    {
        return 1 + collatz(number / 2);
    }
    else
    {
        return 1 + collatz(number * 3 + 1);
    }
}
