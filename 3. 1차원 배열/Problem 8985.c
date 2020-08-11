#include <stdio.h>
#include <string.h>

int main() {
    int n;
    scanf("%d\n", &n);
    char answer[81];
    int score[81] = 0;
    int final = 0;
    for(int i=0; i<n; i++) {
        scanf("%s\n", answer);
        int len = strlen(answer);
        for(int j=0; j<len; j++) {
            if((answer[j]=='O')&&(answer[j+1]=='X')&&(answer[j-1]=='X')) {
                answer[j]=1;
            } else if((answer[j+1]=='O')&&(answer[j]=='O')) {
                score[j+1]=score[j]+1;
            } else {
                score[j]=0;
            }
        }
        for (int k=0; k<len; k++) {
            final = final + score[k];
        }
        printf("%d\n", final);
        final = 0;
        score[81]=0;
    }
    return 0;
}