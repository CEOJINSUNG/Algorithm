// 병합정렬
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int count = 0;

void divide_and_merge(int *array, int left, int right)
{
    int conquer[101];
    int mid = (left + right) / 2;
    int left_index = left;
    int right_index = left;
    int mid_index = mid + 1;

    while (left_index <= mid && mid_index <= right)
    {
        if (array[left_index] <= array[mid_index]) {
            conquer[right_index++] = array[left_index++];
            count++;
        } else {
            conquer[right_index++] = array[mid_index++];
            count++;
        }
    }
    
    if (left_index > mid) {
        while(mid_index <= right) {
            conquer[right_index++] = array[mid_index++];
        }
    } else {
        while(left_index <= mid) {
            conquer[right_index++] = array[left_index++];
        }
    }

    while (left <= right) {
        array[left] = conquer[left];
        left++;
    }
}

void merge_sort(int *array, int left, int right) {
    if (left >= right) {
        return ;
    }

    int mid = (left + right) / 2;
    merge_sort(array, left, mid);
    merge_sort(array, mid + 1, right);
    divide_and_merge(array, left, right);
}


void printf_before(int array[100]) {
    // Before 출력
    printf("Before\n");
    for (int before = 0; before < 100; before++) {
        printf("%2d ", array[before]);
    }
}

void printf_after(int array[100], int count) {
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
    int* random_array = make_random_array();
    printf_before(random_array);
    merge_sort(random_array, 0, 99);
    printf_after(random_array, count);

    count = 0;
    int* ascending_array = make_ascending_array();
    printf_before(ascending_array);
    merge_sort(ascending_array, 0, 99);
    printf_after(ascending_array, count);

    count = 0;
    int* descending_array = make_descending_array();
    printf_before(descending_array);
    merge_sort(descending_array, 0, 99);
    printf_after(descending_array, count);
}