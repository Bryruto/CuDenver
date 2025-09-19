#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //name
    string name =get_string("what is your name? " );

    //age
    int age = get_int ("what is your age? ");

    //hometown
    string hometown =get_string ("what is you hometown? ");

    //phone number
    string number= get_string ("what is you phone number? ");

    printf("My New friends name is %s, %i,they are from %s and their phone number is %s\n",name,age,hometown,number);
    
}
