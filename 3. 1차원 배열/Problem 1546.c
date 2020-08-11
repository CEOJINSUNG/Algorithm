#include <stdio.h>

int main()
{
    int num;
    scanf("%d\n", &num);
    int score[num];
    int max = 0;
    for( int j=0; j<num; j++) {
        scanf("%d", &score[j]); 
        if(score[j]>=max) {
            max = score[j];
        }
    }
    double mid = 0;
    for (int k = 0; k < num; k++)
    {
        mid += score[k] / (double)max * 100;
    }
    mid /= num;
    printf("%f", mid);
    return 0;
}