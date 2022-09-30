// 선택정렬
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void selection_sort(int array[100]) {
    int i, j, temp, max_index;

    // Before 출력
    printf("Before\n");
    for (int before = 0; before < 100; before++) {
        printf("%2d ", array[before]);
    }

    int count = 0;
    for (int i = 0; i < 99; i++){
        max_index = i;
        for (j = i + 1; j < 100; j++) {
            if (array[j] > array[max_index]) {
                max_index = j;
            }
        }
        if (max_index != i) {
            count++;
            temp = array[max_index];
            array[max_index] = array[i];
            array[i] = temp;
        }
    }

    // After 출력
    printf("\n\nAfter Total Change Number: %d 번 실행\n", count);
    for (int after = 0; after < 100; after++) {
        printf("%2d ", array[after]);
    }
    printf("\n\n");
}

int* make_descending_array() {
    static int descend[100];
    for (int i = 1; i <= 100; i++) {
        descend[100-i] = i;
    }
    return descend;
}

int* make_ascending_array() {
    static int ascend[100];
    for (int i = 0; i < 100; i++) {
        ascend[i] = i;
    }
    return ascend;
}

int* make_random_array() {
    static int random[100];
    srand(time(NULL));
    for (int i = 0; i < 100; i++) {
        random[i] = rand()%1000;
    }
    return random;
}


int main() {
    int* descending_array = make_descending_array();
    int* ascending_array = make_ascending_array();
    int* random_array = make_random_array();

    selection_sort(random_array);
    selection_sort(descending_array);
    selection_sort(ascending_array);
}