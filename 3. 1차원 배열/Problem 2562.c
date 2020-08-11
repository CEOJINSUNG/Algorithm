#include <stdio.h>

int main() {
    int a[9];
    int max=1;
    int point=0;
    int i=0;
    while (i<9) {
        scanf("%d\n", &a[i]);
        if (a[i]<=0) {
            continue;
        } else {
            i++;
        }
    }
    for (int j=0; j<9; j++) {
        if(a[j]>=max) {
            max=a[j];
            point = j+1;
        }
    }
    printf("%d\n%d", max, point);
    return 0;
}