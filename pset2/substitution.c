#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool valid_key(string key);

int main(int argc,string argv[])
{
string word;
    if (argc != 2 || !valid_key(argv[1]))
    {
        printf("Key must contain 26 unique alphabetic characters.\n");
        return 1;
    }
    string plaintext = get_string("plaintext: ");
    string ciphertext = plaintext;
    int size = strlen(plaintext);
    for (int i =0;i<size;i++)
    {
        if(isupper(plaintext[i]))
        {
            int index = plaintext[i]- 'A';
            ciphertext[i] = argv[1][index];
            ciphertext[i]=toupper(ciphertext[i]);
        }
        else if (islower(plaintext[i]))
        {
            int index = plaintext[i] - 'a';
            ciphertext[i]=argv[1][index];
           ciphertext[i]=tolower(ciphertext[i]);
        }
    }
 printf("ciphertext:%s\n",ciphertext);
 return 0;
}


bool valid_key(string key)
{
    if (strlen(key) != 26)
    {
        return false;
    }

    int letters[26] = {0};

    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
        {
            return false;
        }

        int index = toupper(key[i]) - 'A';
        if (letters[index]++)
        {
            return false; // Duplicate letter
        }
    }
    return true;
}
