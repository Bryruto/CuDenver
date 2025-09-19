#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Ask for text
    string Text = get_string("Text: ");

    // Set variables
    int size = strlen(Text);
    int word = 1;       // Start at 1 because the first word doesn't follow a space
    int sen = 0;        // Sentence counter
    int letter = 0;     // Letter counter
    double avgl = 0.0;
    double avgs = 0.0;

    // Count letters, words, and sentences
    for (int i = 0; i < size; i++)
    {
        if (word != 100)
        {
            if (Text[i] == ' ')
            {
                word++;
            }
            else if (Text[i] == '.' || Text[i] == '!' || Text[i] == '?')
            {
                sen++;
            }

            if (isalpha(Text[i]))
            {
                letter++;
            }
        }
    }

    // Calculate averages per 100 words
    avgl = ((double)letter / word) * 100;
    avgs = ((double)sen / word) * 100;

    // Coleman-Liau index formula
    double index = 0.0588 * avgl - 0.296 * avgs - 15.8;
    index = round(index);

    // Output grade level
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int)index);
    }

    return 0;
}

