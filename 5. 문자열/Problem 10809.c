#include <stdio.h>
#include <string.h>

int main() {
    char alpha[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    char word[101];
    scanf("%s", word);
    int len = strlen(word);
    int cnt=-1;
    for(int i=0; i<26; i++){
        for(int j=0; j<len; j++) {
            if(alpha[i]==word[j]) {
                cnt=j;
                break;
            }
        }
        printf("%d ", cnt);
        cnt=-1;
    }
    return 0;
}