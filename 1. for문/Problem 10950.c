#include <stdio.h>

int main() {
    int N;
    int a, b, c;
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        scanf("%d %d\n", &a, &b);
        c = a+b;
        printf("%d\n", c);
    }
}