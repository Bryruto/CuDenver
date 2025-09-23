#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int points(string score);

int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int main(void)
{
    // Prompt the user for two words
    int score1, score2;
    string word1 = get_string("Player1: ");
    string word2 = get_string("Player2: ");

    // Compute the score of each word
    score1 = points(word1);
    score2 = points(word2);

    // Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int points(string score)
{
    int total = 0;
    int size = strlen(score);
    for (int i = 0; i < size; i++)
    {
        if (isalpha(score[i]))
        {
            if (islower(score[i]))
            {
                score[i] = toupper(score[i]);
            }
            total = POINTS[score[i] - 'A'] + total;
        }
    }
    return total;
}
