#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long card;
    int digits[18];
    int new[18];
    int plus = 0;
    int adds2 = 0;

    // Get card number
    card = get_long("Number: ");

    if (card < 1000000000000 || card > 9999999999999999)
    {
        printf("INVALID\n");
        return 0;
    }


    // Count digits and reverse them into array
    long temp = card;
    int count = 0;
    while (temp > 0)
    {
        digits[count++] = temp % 10;
        temp /= 10;
    }

    // Double every second digit from the right (i.e., digits[1], [3], etc.)
    for (int p = 1; p < count; p += 2)
    {
        int doubled = digits[p] * 2;
        if (doubled >= 10)
        {
            new[plus++] = doubled / 10;
            new[plus++] = doubled % 10;
        }
        else
        {
            new[plus++] = doubled;
        }
    }

    // Add the non-multiplied digits
    for (int q = 0; q < count; q += 2)
    {
        adds2 += digits[q];
    }

    // Add the split digits
    for (int w = 0; w < plus; w++)
    {
        adds2 += new[w];
    }

    // Luhn check
    if (adds2 % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    // Get first and first two digits
    int first_digit = digits[count - 1];
    int second_digit = digits[count - 2];
    int first_two_digits = first_digit * 10 + second_digit;

    // Determine card type
    if (count == 15 && (first_two_digits == 34 || first_two_digits == 37))
    {
        printf("AMEX\n");
    }
    else if (count == 16 && (first_two_digits >= 51 && first_two_digits <= 55))
    {
        printf("MASTERCARD\n");
    }
    else if ((count == 13 || count == 16) && first_digit == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
