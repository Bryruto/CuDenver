// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"
int time_amount = 0;
// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 17576;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int i = hash(word);
    node *cursor = table[i];
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int index = 0;
    int amount[3]={0,0,0};
    // TODO: Improve this hash function
for (int i =0;i < 3 && i < strlen(word);i++)
{
    amount[i] = toupper(word[i])-'A';
}
if (strlen(word)==2)
{
    index = amount[0] *26 + amount[1];
}
else if (strlen(word)==1)
{
    index = amount[0];
}
else if (strlen(word)==3)
{
    index = amount[0] *26 *26 + amount[1] *26 + amount[2];
}
    return index;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // open dictionary file
    FILE *file = fopen(dictionary, "r");
    // check if it is null
    if (file == NULL)
    {
        return false;
    }
    char tmp[LENGTH + 1];
    // read strings form file one at a time
    while (fscanf(file, "%s", tmp) != EOF)
    {
        // create a new node for each word
        node *new = malloc(sizeof(node));
        strcpy(new->word, tmp);
        if (new == NULL)
        {
            return false;
        }
        // hash word to obtain a hash value
        int i = hash(new->word);
        // insert node into hash table at that location
        new->next = table[i];
        table[i] = new;
        time_amount++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return time_amount;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *msFree = table[i];
        node *cursor = table[i];
        while (cursor != NULL)
        {
            cursor = cursor->next;
            free(msFree);
            msFree = cursor;
        }
        table[i] = NULL;
    }
    return true;
}
