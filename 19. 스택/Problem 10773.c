#include <stdio.h>

int stack[100000];
int main() {
    int K, top=0;
    int sum = 0;
    scanf("%d", &K);
    for (int i=0; i<K; i++) {
        int number;
        scanf("%d", &number);
        if (number != 0) {
            stack[top] = number;
            top++;
            sum += number;
        } else {
            sum -= stack[top-1];
            top--;
        }
    }
    printf("%d", sum);
    return 0;
}