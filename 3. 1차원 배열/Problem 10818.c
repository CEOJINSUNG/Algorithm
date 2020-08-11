#include <stdio.h>

int main() {
    int n;
    int a[2000000];
    int max, min;
    scanf("%d", &n);
    if((1<=n)&&(n<=1000000)) {
        for(int i=0; i<n; i++) {
            scanf("%d", &a[i]);
            if ((-1000000<=a[i])&&(a[i]<=1000000)) {
                continue;
            } else {
                break;
            }
        }
        max=a[0];
        min=a[n-1];
        for (int i=0; i<n; i++) {
            if(a[i]>max) {
                max=a[i];
            }
            if(a[i]<min) {
                min = a[i];
            }
        }
    }
    printf("%d %d", min, max);
    return 0;
}