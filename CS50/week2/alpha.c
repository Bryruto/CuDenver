#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    // Get user input
    if (argc !=2)
    {
        printf("please provide a word.\n");
        return 1;
    }
    
    string word =argv[1];
    int size = strlen(word);

    for (int j = 0; j < size; j++)
    {
        if (isupper(word[j]))
        {
            word[j] = tolower(word[j]);
        }
    }
    for (int i = 0; i < size - 1; i++)
    {
        if (word[i] > word[i + 1])
        {
            printf("No\n");
            return 0;
        }
    }
    printf("yes\n");
}
