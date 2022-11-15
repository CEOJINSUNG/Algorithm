// 개방 주소법
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int m = 37;

// h'(k) = k mod m
int basic_modular(int k) {
    return k % m;
}

// linear probing
int linear(int k, int i) {
    return (basic_modular(k) + i) % m;
}

// quadratic probing
int quadratic(int k, int i) {
    return (basic_modular(k) + i + 3 * i * i) % m;
}

// double hashing
int double_hashing(int k, int i) {
    return (basic_modular(k) + i * (1 + k % (m - 1))) % m;
}

void open_addressing(char type, int array[30]) {
    int hash_table[m];
    int probes[m];

    // 초기화
    for (int i = 0; i < m; i++) {
        hash_table[i] = 0;
        probes[i] = 0;
    }

    // 연산 수행
    for (int i = 0; i < 30; i++) {
        for (int j = 0; j < m; j++) {
            int num = 0;
            switch (type) {
                case 'l':
                    num = linear(array[i], j);
                    break;
                case 'q':
                    num = quadratic(array[i], j);
                    break;
                case 'd':
                    num = double_hashing(array[i], j);
                default:
                    break;
            }

            if (hash_table[num] == 0) {
                hash_table[num] = array[i];
                probes[num] = i;
                break;
            }
        }
    }

    // 0 ~ m 까지 hash table과 평균 probe 값과 가장 큰 probe 값 출력
    int total = 0;
    for (int i = 0; i < m; i++) {
        printf("%d, ", hash_table[i]);
        
        int probe = probes[i];
        total = total + probe;
    }

    // Primary Cluster Length
    int length = 0;
    int max_length = 0;
    for (int i = 0; i < m; i++) {
        if (hash_table[i] != 0) {
            length++;
            if (length > max_length) {
                max_length = length;
            }
        } else {
            length = 0;
        }
    }

    printf("\n평균 probes per insertion : %d\n", total / 30);
    printf("Primary Cluster Length : %d\n", max_length);
}

void make_random_array(int random[30]) {
    int i, j;
    srand((unsigned int) time(NULL));
    for (i = 0; i < 30; i++) {
        random[i] = rand()%1000;
        for (j = 0; j < i; j++) {
            if (random[i] == random[j]) {
                i--;
                break;
            }
        }
    }
}

int main() {
    // 1) linear probing
    printf("linear probing 수행 \nHash Table 결과 - ");
    int case1[30];
    make_random_array(case1);
    open_addressing('l', case1);

    // 2) quadratic probing
    printf("\nquadratic probing 수행 \nHash Table 결과 - ");
    int case2[30];
    make_random_array(case2);
    open_addressing('q', case2);

    // 3) double hashing
    printf("\ndouble hashing 수행 \nHash Table 결과 - ");
    int case3[30];
    make_random_array(case3);
    open_addressing('d', case3);
}