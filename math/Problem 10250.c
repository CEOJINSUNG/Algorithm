#include <stdio.h>

int main () {
    int h, w, n, num;
    scanf("%d", &num);
    for (int i=0; i<num; i++) {
        scanf("%d %d %d\n", &h, &w, &n);
        if (n%h == 0) {
            printf("%d\n", h*100+n/h);
        } else {
            printf("%d\n", (n%h)*100+n/h+1);
        }
    }
    return 0;
}