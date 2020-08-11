#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    if ((1<=N)&&(N<=10000)){
        int a;
        a = 0;
        int b = N+1;
        for(int i=1; i<b; i++) {
            a = a + i;
        }
        printf("%d", a);
    }
}