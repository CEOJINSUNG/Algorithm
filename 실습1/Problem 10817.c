#include<stdio.h>

int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    
    if(a-b>=0&&b-c>=0)
        printf("%d", b);
    else if(c-b>=0&&b-a>=0)
        printf("%d", b);
    else if(a-c>=0&&c-b>=0)
        printf("%d", c);
    else if(b-c>=0&&c-a>=0)
        printf("%d", c);
    else if(b-a>=0&&a-c>=0)
    printf("%d", a);
    else if(c-a>=0&&a-b>=0)
    printf("%d", a);
    
}