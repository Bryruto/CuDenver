#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            BYTE grayscales =
                round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtBlue = grayscales;
            image[i][j].rgbtGreen = grayscales;
            image[i][j].rgbtRed = grayscales;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;

            int sepiaRed =
                round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue);
            int sepiaGreen =
                round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue);
            int sepiaBlue =
                round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue);

            image[i][j].rgbtRed = (sepiaRed > 255) ? 255 : sepiaRed;
            image[i][j].rgbtGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;
            image[i][j].rgbtBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE pass[height][width];
    for (int i = 0; i < height; i++)
    {
        int tmp = width - 1;
        for (int j = 0; j < width; j++)
        {
            pass[i][tmp].rgbtRed = image[i][j].rgbtRed;
            pass[i][tmp].rgbtGreen = image[i][j].rgbtGreen;
            pass[i][tmp].rgbtBlue = image[i][j].rgbtBlue;
            tmp--;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = pass[i][j].rgbtRed;
            image[i][j].rgbtGreen = pass[i][j].rgbtGreen;
            image[i][j].rgbtBlue = pass[i][j].rgbtBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int redTotal = 0;
            int greenTotal = 0;
            int blueTotal = 0;
            int count = 0;

            // Check all 3x3 neighboring pixels
            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    // Ensure we don't go out of bounds
                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        redTotal += image[ni][nj].rgbtRed;
                        greenTotal += image[ni][nj].rgbtGreen;
                        blueTotal += image[ni][nj].rgbtBlue;
                        count++;
                    }
                }
            }

            temp[i][j].rgbtRed = round((float) redTotal / count);
            temp[i][j].rgbtGreen = round((float) greenTotal / count);
            temp[i][j].rgbtBlue = round((float) blueTotal / count);
        }
    }

    // Copy blurred result back
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
}
