#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
     string strings[] = {"aa","bb","cc"};

     string s = get_string("letter ");
for (int i=0;i<3;i++)
{
     if (strcmp(strings[i],s)==0)
     {
          printf("found\n");
          return 0;
     }
}
     printf("not found\n");
}
