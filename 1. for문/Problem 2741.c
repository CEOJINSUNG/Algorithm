#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    if((1<=N)&&(N<=100000)) {
        for (int i=1; i<= N; i++) {
            printf("%d\n", i);
        }
    }
}