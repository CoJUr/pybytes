#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char c = get_char("Do you agree? ");

    if (c == 'y' || c == 'Y')
    {
        printf("Agree.\n");
    }
    else if (c == 'n' || c == 'N')
    {
        printf("Not agreed.\n");
    }
}
int main(void)
{
    printf("meow\n");
    printf("meow\n");
    printf("meow\n");

    int counter = 3;
    while (counter > 0)
    {
        printf("meow\n");
        counter = counter -1;
    }
}

