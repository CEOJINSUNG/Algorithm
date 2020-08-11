#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);
    for(int i=1; i<=T; i++) {
        int A, B;
        scanf("%d %d\n", &A, &B);
        if ((0<A)&&(A<10)&&(0<B)&&(B<10)){
            int C = A+B;
            printf("Case #%d: %d + %d = %d\n", i, A ,B, C);
        }
    }
}