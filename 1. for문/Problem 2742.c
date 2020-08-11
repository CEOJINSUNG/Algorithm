#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    if ((1<=N)&&(N<=100000)) {
        for(int i=N; i>0; i--) {
            printf("%d\n", i);
        }
    }
}