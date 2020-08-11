#include <stdio.h>

int main() {
    int hour, min;
    scanf("%d %d", &hour, &min);
    if (min-45 >=0) {
        printf("%d %d", hour, min-45);
        return 0;
    }
    else {
        if (hour==0) {
            printf("23 %d", min+15);
            return 0;
        }
        printf("%d %d", hour-1, min+15);
        return 0;
    }
}