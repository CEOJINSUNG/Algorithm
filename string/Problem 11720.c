#include <stdio.h>

int main() {
    int n;
    int sum=0;
    char num[101];
    scanf("%d\n", &n);
    scanf("%s", num);
    for (int i=0; i<n; i++) {
        sum = sum + num[i] - '0';
    }
    printf("%d", sum);
    return 0;
}