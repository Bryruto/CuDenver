#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    int votes;
}
candidate;
int main(void)
{
string winner;
const int num =3;
candidate candidates[num];

for (int i=0;i<num;i++)
{
    candidates[i].name = get_string("Name: ");
    candidates[i].votes = get_int("votes: ");
}
int highest_vote =0;
for (int i=0;i<num;i++)
{
    if(candidates[i].votes >highest_vote)
    {
        highest_vote =candidates[i].votes;
    }
}
for (int i =0;i<num;i++)
{
    if (candidates[i].votes == highest_vote)
    {
        printf("%s is the winner\n",candidates[i].name);
    }
}
}
