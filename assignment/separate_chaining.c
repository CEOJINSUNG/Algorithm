// 분리 연결법
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void separate_chaining(int m, int array[50]) {
    int hash_table[m][50];

    // 초기화
    for (int i = 0; i < m; i++) {
        for(int j = 0; j < 50; j++) {
            hash_table[i][j] = 0;
        }
    }

    // 랜덤 배열 삽입
    for (int i = 0; i < 50; i++) {
        int num = array[i]%m;
        for (int j = 0; j < 50; j++) {
            int current = hash_table[num][j];
            if (current == 0) {
                hash_table[num][j] = array[i];
                break;
            }
        }
    }

    // 가장 짧고, 길고, 평균 길이 산출
    int shortest = 51;
    int longest = 0;
    int total = 0;
    
    for (int i = 0; i < m; i++) {
        int length = 0;

        for (int j = 0; j < 50; j++) {
            if (hash_table[i][j] != 0) {
                length++;
            } else {
                break;
            }
        }

        if (length < shortest) {
            shortest = length;
        }

        if (length > longest) {
            longest = length;
        }

        total = total + length;
    }

    printf("\n현재 Hash Function : k mod %d\n", m);
    printf("가장 짧은 체인의 길이 : %d\n", shortest);
    printf("가장 긴 체인의 길이 : %d\n", longest);
    printf("체인 길이 평균 (기준 : 나누고 남은 몫) : %d\n", total / m);
}

int* make_random_array() {
    static int random[50];
    int i, j;
    srand((unsigned int) time(NULL));
    for (i = 0; i < 50; i++) {
        random[i] = rand()%1000;
        for (j = 0; j < i; j++) {
            if (random[i] == random[j]) {
                i--;
                break;
            }
        }
    }
    return random;
}

int main() {
    // 1) k mod 5
    int* case1 = make_random_array();
    separate_chaining(5, case1);

    // 2) k mod 7
    int* case2 = make_random_array();
    separate_chaining(7, case2);

    // 3) k mod 13
    int* case3 = make_random_array();
    separate_chaining(13, case3);
}