#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        return 1;
    }

    uint8_t buffer[512];
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        return 1;
    }

    FILE *output = NULL;
    char filename[8];
    int jpeg_count = 0;

    while (fread(buffer, sizeof(uint8_t), 512, input) == 512)
    {
        // Check for JPEG header
        if (buffer[0] == 0xFF && buffer[1] == 0xD8 && buffer[2] == 0xFF && (buffer[3] & 0xF0) == 0xE0)
        {
            // If already writing a JPEG, close it
            if (output != NULL)
            {
                fclose(output);
            }

            // Create a new filename and open a new file
            sprintf(filename, "%03i.jpg", jpeg_count++);
            output = fopen(filename, "w");
        }

        // If a JPEG file is open, write the block
        if (output != NULL)
        {
            fwrite(buffer, sizeof(uint8_t), 512, output);
        }
    }

    // Close any open files
    if (output != NULL)
    {
        fclose(output);
    }
    fclose(input);
    return 0;
}

