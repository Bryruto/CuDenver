#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("What's your name? ");//ask for name

    printf("hello, %s\n",name);//hello then name
}
