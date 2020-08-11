#include <stdio.h>

int main() {
    int score[5];
    int mid=0;
    for (int i=0; i<5; i++) {
        scanf("%d\n", &score[i]);
        if(score[i]<40) {
            score[i] = 40;
        }
        mid += score[i];
    }
    mid /= 5;
    printf("%d", mid);
    return 0;
}