#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main() {
    int gb[11] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000 };
    int n;
    int temp = 0;
    for (int i = 0; i < 3; i++) { // 몇번째로 입력받는 숫자인지 확인하는 장치가 된다.
        char n1[10];

        scanf("%s", &n1);

        if ((strcmp("black", n1) == 0)) { // 입력받은 문자가 원하는 문자가 맞는지 확인
            n = 0;} //여기서의 n은 1의 자리나 10의 자리나 모두 0이므로 그냥 0이 된다.
        else if ((strcmp("brown", n1) == 0)) {
            if (i == 1 || i == 2)
                n = 1; 
            else n = 10;}
        else if ((strcmp("red", n1) == 0)) {
            if (i == 1 || i == 2)
                n = 2; 
            else n = 20; }
        else if ((strcmp("orange", n1) == 0)) {
            if (i == 1 || i == 2)
                n = 3; 
            else n = 30; }
        else if ((strcmp("yellow", n1) == 0)) {
            if (i == 1 || i == 2)
                n = 4; 
            else n = 40; }
        else if ((strcmp("green", n1) == 0)) {
            if (i == 1 || i == 2)
                n = 5; 
            else n = 50; }
        else if ((strcmp("blue", n1) == 0)) {
            if (i == 1 || i == 2)
                n= 6; 
            else n = 60; }
        else if ((strcmp("violet", n1) == 0)) {
            if (i == 1 || i == 2)
                n = 7; 
            else n = 70; }
        else if ((strcmp("grey", n1) == 0)) {
            if (i == 1 || i == 2)
                n = 8; 
            else n = 80; }
        else if ((strcmp("white", n1) == 0)) { 
            if (i == 1 || i == 2)
                n = 9; 
            else n = 90; }
        temp += n; //temp라는 변수를 이용해서 두개의 숫자를 받아 합연산을 진행
    }
    printf("%.0f",(double)(temp - n) * gb[n]); // 곱해야 할 수는 배열의 인덱스를 이용해서 곱하고, 출력값을 설정해준다.
    return 0;
}

