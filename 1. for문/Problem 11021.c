#include <stdio.h>

int main(void) {
    int T;
    scanf("%d\n", &T);
    for (int i=1; i<=T; i++){
        int A, B;
        scanf("%d %d\n", &A, &B);
        if ((0<A)&&(A<10)&&(0<B)&&(B<10)){
            int C = A+B;
            printf("Case #%d: %d\n", i, C);
        }
    }
    return 0;
}