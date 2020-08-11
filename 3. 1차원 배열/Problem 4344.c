#include <stdio.h>
#include <math.h>

int main() {
    int n, num;
    int mid=0;
    int cnt=0;
    double rate;
    scanf("%d\n", &n);
    for (int i=0; i<n; i++) {
        scanf("%d", &num);
        int score[1000];
        for(int j=0; j<num; j++) {
            scanf("%d", &score[j]);
            mid += score[j];
        }
        double avg =  (double) mid/num;
        for (int k=0; k<num; k++) {
            if(score[k]> avg) {
                cnt++;
            }
        }
        rate = (double)cnt/(double)num*100;
        double nearest = roundf(rate*1000)/1000;
        printf("%.3f%%\n", nearest);
        mid = 0;
        cnt = 0;
        score[1000] =0;
    }
    return 0;
}