#include <stdio.h>

int fibonacci(int a) {
    if(a==0) return 0;
    else if (a==1) return 1;
    else
    {
        return fibonacci(a-1)+fibonacci(a-2);
    }
}

int main() {
    int num1=0;
    int num2=1;
    int num3;
    int k;
    scanf("%d", &k);
    for(int i=2; i<k; i++) {
        fibonacci(i);
    }
    printf("%d", fibonacci(k));
    return 0;
}