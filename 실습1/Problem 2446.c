#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int a, b, c, d;
    for (int k=n; k>0; k--) {
        a=2*k-1;
        b=n-k;
        for(int l=0; l<b; l++) {
            printf(" ");
        }
        for(int m=a; m>0; m--) {
            printf("*");
        }
        printf("\n");
    }
    for(int i=1; i<n; i++) {
        c=2*i+1;
        d=n-i-1;
        for(int w=0; w<d; w++) {
            printf(" ");
        }
        for(int j=0; j<c; j++) {
            printf("*");
        }
        printf("\n");
    }
}