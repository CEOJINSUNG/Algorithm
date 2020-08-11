#include <stdio.h>

int main()
{
    int n, x;
    scanf("%d %d\n", &n, &x);
    if ((1 <= n) && (n <= 10000) && (1 <= x) && (x <= 10000))
    {
        int a[n];
        int b[10000];
        int j=0;
        for (int i = 0; i < n; i++)
        {
            scanf("%d ", &a[i]);
            if (a[i] < x)
            {
                b[j]=a[i];
                pritnf("%d ", b[j]);
                j++;
            }
        }
    }
    return 0;
}