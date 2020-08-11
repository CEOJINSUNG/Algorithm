#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d\n%d\n%d", &a, &b, &c);
    int num = a*b*c;
    int m[9]={-1,-1,-1,-1,-1,-1,-1,-1,-1};
    for (int i=0; i<9; i++) {
        m[i] = num%10;
        num /= 10;
        if(num==0) {
            break;
        }
    }
    for (int j=0; j<10; j++) {
        int count=0;
        for(int k=0; k<9; k++) {
            if(m[k]==j) {
                count++;
            }
        }
        printf("%d\n", count);
    }
    return 0;
}