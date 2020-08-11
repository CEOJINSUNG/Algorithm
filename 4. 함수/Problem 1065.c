#include <stdio.h>
#include <math.h>

#define size 1000

int count(int num) {
    int i, cnt=0;
    for ( i = 100; i <= num; i++)
    {
        if((i/100-i/10%10)==(i/10%10-i%10)) {
            cnt++;
        }
    }
    return cnt;
    
}

int main() {
    int n, a;
    scanf("%d", &n);
    if (n==1000)
    {
        a = count(n-1);
        a += 99;
    }
    else
    {
        if (n/100 != 0)
        {
            a=count(n);
            a += 99;
        }
        else
        {
            a=n;
        }
    }
    printf("%d\n", a);
    return 0;
}