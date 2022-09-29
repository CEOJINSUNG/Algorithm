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

    for (int i = 0; i < 99; i++){
        max_index = i;
        for (j = i + 1; j < 100; j++) {
            if (array[j] > array[max_index]) {
                max_index = j;
            }
        }
        temp = array[max_index];
        array[max_index] = array[i];
        array[i] = temp;
    }

    // After 출력
    printf("\nAfter");
    for (int after = 0; after < 100; after++) {
        printf("%2d ", array[after]);
    }
}

int main() {
    int array[100] = {0, };
    selection_sort(array);
}