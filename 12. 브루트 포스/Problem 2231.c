#include <stdio.h>
#include <math.h>

int main() {
    int n, result = 0;
    scanf("%d", &n);
    int sum = 0;
    for (int i=1; i<n; i++) {
        sum = 0;
        for (int j=5; j>=0; j--)
            sum += (i / (int)pow(10, j)%10);
        sum += i;
        if(sum == n) {
            result = i;
            break;
        }
    }
    printf("%d\n", result);
    return 0;
}