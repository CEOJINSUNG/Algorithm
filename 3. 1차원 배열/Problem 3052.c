#include <stdio.h>

int main() {
    int a[10];
    int b[10];
    int d[10];
    int e = 0;
    for (int i=0; i<10; i++) {
        scanf("%d\n", &a[i]);
        b[i] = a[i]%42;
    }
    for (int j=0; j<10; j++) {
        int c=0;
        int k = j+1;
        while (k<10) {
            if(b[j] == b[k]) {
                c++;
            }
            k++;
        }
        d[j] = c;
    }
    for (int m=0; m<10; m++){
        if(d[m]==0) {
            e++;
        }
    }

    printf("%d", e);
    return 0;
}