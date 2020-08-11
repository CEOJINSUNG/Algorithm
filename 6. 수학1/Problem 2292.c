#include <stdio.h>

int main () {
    int num;
    scanf("%d", &num);
    int count = 1;
    int i = 0;
    while (1) {
        if(num<=count) {
            printf("%d", i+1);
            break;
        }
        i++;
        count = count + 6*i;
    }
    return 0;
}