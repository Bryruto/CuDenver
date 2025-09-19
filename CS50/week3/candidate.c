#include <cs50.h>
#include <string.h>
#include <stdio.h>

typedef struct
{
string name;
int vote;
}
candidate;

int main(void)
{
string winner;
candidate candidates[] = {{"brycen", 0},{"caden", 0},{"kylie", 0}};
int times = get_int("how many voters: ");
for (int i=0;i<times;i++)
{
string voter= get_string("Vote: ");
if (strcmp(candidates[0].name,voter)==0)
{
    candidates[0].vote++;
}
else if (strcmp(candidates[1].name,voter)==0)
{
    candidates[1].vote++;
}
else if(strcmp(candidates[2].name,voter)==0)
{
    candidates[2].vote++;
}
}
for(int i =0;i<2;i++)
{
    if (candidates[i].vote>candidates[i+1].vote)
    {
        winner= candidates[i].name;
    }
    else if(candidates[i].vote>candidates[i+1].vote)
    {
        winner= candidates[i].name;
    }
}
printf("Winner:%s\n",winner);

}
