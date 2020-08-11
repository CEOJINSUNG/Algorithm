#include <stdio.h>

int main()
{
    int T;
    scanf("%d\n", &T);

    if ((1 <= T) && (T <= 10000000))
    {
        for (int i = 0; i < T; i++)
        {
            int a, b;
            scanf("%d %d\n", &a, &b);
            if ((1 <= a) && (a <= 1000) && (1 <= b) && (b <= 1000))
            {
                int c = a + b;
                printf("%d\n", c);
            }
        }
    }
}