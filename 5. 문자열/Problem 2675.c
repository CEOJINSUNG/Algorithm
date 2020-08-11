#include <stdio.h>
#include <string.h>

int main() {
    int num;
    int repeat;
    char word[21];
    scanf("%d", &num);
    for(int i=0; i<num; i++) {
        scanf("%d ", &repeat);
        scanf("%s", word);
        int len = strlen(word);
        for(int j=0; j<len; j++) {
            for(int k=0; k<repeat; k++) {
                printf("%c", word[j]);
            }
        }
        printf("\n");
    }
    return 0;
}