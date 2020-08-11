#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for(int i=1; i<=n; i++) {
        for(int j=0; j<i; j++) {
            printf("*");
        }
        printf("\n");
    }
    for (int k=0; k<n-1; k++) {
        for(int m=n-1; m>k; m--) {
            printf("*");
        }
        printf("\n");
    }
}