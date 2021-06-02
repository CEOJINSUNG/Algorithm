#include <stdio.h>

int main() {
    int n, m;
    int sum, max = 0;
    scanf("%d %d", &n, &m);
    int card[n];
    for (int i=0; i<n; i++) {
        scanf("%d", &card[i]);
    }
    for (int j=0; j<n; j++) {
        for (int k=j+1; k<n; k++) {
            for (int l=k+1; l<n; l++) {
                sum = card[j] + card[k] + card[l];
                if (sum > max && sum <=m) {
                    max = sum;
                }
            }
        }
    }
    printf("%d", max);
    return 0;
}