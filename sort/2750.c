#include <stdio.h>

int swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void selectionSort(int arr[], int size) {
    int minIndex;
    int i, j;
    for (i = 0; i<size-1; i++) {
        minIndex = i;
        for (j=i+1; j<size; j++) {
            if(arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        swap(&arr[i], &arr[minIndex]);
    }
}

int main() {
    int N;
    int arr[1000];
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        scanf("%d", &arr[i]);
    }
    selectionSort(arr, N);

    for(int j=0; j<N; j++) {
        printf("%d\n", arr[j]);
    }
    
    return 0;
}
