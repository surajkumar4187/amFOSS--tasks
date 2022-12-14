#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    int height;
    do
    {
    heightoftriangle = get_int("please enter your triangle height here: \n");
    }

    while 
    ((heightoftriangle < 1) || (heightoftriangle > 8)); 

    for (int horizontal_length = 0; horizontal_length < heightoftriangle; horizontal_length++)
    {

        for (int column_length = 0; column_length < heightoftriangle; column_length++)
        {

            if (horizontal_length + column_length >= heightoftriangle - 1) 
                printf("#");

            else 
            printf(" ");
        }
        printf("\n");
    }
}
