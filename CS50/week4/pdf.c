#include <stdio.h>
#include <stdint.h>
#include <stdio.h>

int main(int argc,char *argv[])
{
if (argc != 2)
{
    printf("Please give a file\n");
    return 1;
}
//open file
FILE *input =fopen(argv[1],"r");

//create a buffer
uint8_t buffer[4];

//create an array of signature bytes
uint8_t signature[]={0x25,0x50,0x44,0x46};

//ready first 4 bytes from the file
fread(buffer,sizeof(uint8_t),4,input);

//check the first 4 bytes again signature bytes
for (int i=0;i<4;i++)
{
    if (signature[i] != buffer[i])
    {
        printf("Not a pdf\n");
        return 0;
    }
}

//sucess!
printf("is a pdf\n");

//close the file
fclose(input);

return 0;
}
