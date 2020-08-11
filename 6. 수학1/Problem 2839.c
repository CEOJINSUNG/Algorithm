#include <stdio.h>

int main()
{
    int a, b, c;
    scanf("%d", &a);
    b = a / 5;
    c = a % 5;
    if (c == 0)
    {
        printf("%d", b);
        return 0;
    }
    for (; b > 0; b--)
    {
        if (c % 3 == 0)
        {
            printf("%d", (c / 3) + b);
            return 0;
        }
        c = c + 5;
    }
    if (a % 3 == 0)
    {
        printf("%d", a / 3);
        return 0;
    }
    printf("%d", -1);
    return 0;
}