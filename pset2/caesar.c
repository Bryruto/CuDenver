#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    for (int x=0;x<strlen(argv[1]);x++)
    {
    if (!isdigit(argv[1][x]))
    {
        return 1;
    }
    }
    int key = atoi(argv[1]);
    string plaintext = get_string("plaintext: ");

    for (int i = 0, times = strlen(plaintext); i < times; i++)
    {
        if (isalpha(plaintext[i]))
        {
            char base = isupper(plaintext[i]) ? 'A' : 'a';
            plaintext[i] = (plaintext[i] - base + key) % 26 + base;
        }
    }

    printf("ciphertext: %s\n", plaintext);
    return 0;
}
