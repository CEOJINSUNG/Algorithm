#include <stdio.h>

int main() {
    int a, b;
    while (true) {
        scanf("%d %d\n", &a,&b);
        if((a==0)&&(b==0)) {
            break;
        }
        int c = a+b;
        printf("%d\n", c);
    }
    return 0;
}