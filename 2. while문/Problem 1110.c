#include <stdio.h>

int main()
{
    int n;
    int a, b;
    int i = 0;
    scanf("%d\n", &n);
    if ((0<=n)&&(n<=99))
    {
        a = n/10;
        b = n % 10;
        while (1)
        {
            int d = a + b;
            int f = d%10;
            int e = b * 10 + f;
            i++;
            if (e == n)
            {
                printf("%d", i);
                break;
            }
            else
            {
                a=e/10;
                b=e%10;
            }
        }
    } else {
        return 0;
    }
    return 0;
}