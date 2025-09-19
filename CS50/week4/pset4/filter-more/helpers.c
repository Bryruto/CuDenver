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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp[height][width];

    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};

    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            tmp[i][j].rgbtRed = image[i][j].rgbtRed;
            tmp[i][j].rgbtGreen = image[i][j].rgbtGreen;
            tmp[i][j].rgbtBlue = image[i][j].rgbtBlue;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int gxRed = 0;
            int gyRed = 0;
            int gxGreen = 0;
            int gyGreen = 0;
            int gxBlue = 0;
            int gyBlue = 0;

            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    if (ni < 0 || ni >= height || nj < 0 || nj >= width)
                        continue;

                    int weight = Gx[di + 1][dj + 1];
                    int value = tmp[ni][nj].rgbtRed;
                    gxRed += weight * value;
                    value = tmp[ni][nj].rgbtGreen;
                    gxGreen += weight * value;
                    value = tmp[ni][nj].rgbtBlue;
                    gxBlue += weight * value;

                    weight = Gy[di + 1][dj + 1];
                    value = tmp[ni][nj].rgbtRed;
                    gyRed += weight * value;
                    value = tmp[ni][nj].rgbtGreen;
                    gyGreen += weight * value;
                    value = tmp[ni][nj].rgbtBlue;
                    gyBlue += weight * value;
                }
            }
            int redValue = round(sqrt(gxRed * gxRed + gyRed * gyRed));
            int greenValue = round(sqrt(gxGreen * gxGreen + gyGreen * gyGreen));
            int blueValue = round(sqrt(gxBlue * gxBlue + gyBlue * gyBlue));
            if (redValue > 255)
            {
                redValue = 255;
            }
            if (greenValue > 255)
            {
                greenValue = 255;
            }
            if (blueValue > 255)
            {
                blueValue = 255;
            }
            if (redValue < 0)
            {
                redValue = 0;
            }
            if (greenValue < 0)
            {
                greenValue = 0;
            }
            if (blueValue < 0)
            {
                blueValue = 0;
            }
            image[i][j].rgbtRed = redValue;
            image[i][j].rgbtGreen = greenValue;
            image[i][j].rgbtBlue = blueValue;
        }
    }

    return;
}
