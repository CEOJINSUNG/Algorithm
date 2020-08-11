#include <stdio.h>

int main()
{
    int a, b;
    while (scanf("%d %d\n", &a, &b) != EOF)
    {
        if ((0 < a) && (a < 10) && (0 < b) && (b < 10))
        {
            int c = a+b;
            printf("%d\n", c);
        }
        else {
            break;
        }
    }
    return 0;
}