#include <stdio.h>

int main() {
    int burger[3];
    int minbur = 2000;
    int bever[2];
    int minbe = 2000;
    for (int i=0; i<3; i++) {
        scanf("%d", &burger[i]);
        if (burger[i] <= minbur) {
            minbur = burger[i];
        }
    }
    for(int j=0; j<2; j++) {
        scanf("%d", &bever[j]);
        if (bever[j] <= minbe) {
            minbe = bever[j];
        }
    }
    printf("%d", minbe+minbur-50);
    return 0;
}