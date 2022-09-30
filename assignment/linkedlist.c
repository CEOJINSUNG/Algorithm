#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void insert(int* array, int index, int inserted_data) {
    memmove(array + index + 1, array + index, sizeof(int) * (60 - index));
    array[index] = inserted_data;
}

void delete(int* array) {
    int count = 0;
    for (int i = 59; i > -1; i--) {
        if (array[i] != -1) {
            count++;
            if (count == 3) {
                array[i] = -1;
                break;
            }
        }
    }
}

void print(int* array) {
    int count = 0;
    for (int i = 0; i < 60; i++) {
        if (count >= 9) {
            break;
        }
        if (array[i] != -1) {
            count++;
            if (count%3 == 0 ) {
                printf("%d\n", array[i]);
            }
        } 
    }
}

void print_array(int* array) {
    for (int i = 0; i < 3; i++) {
        if (array[i] != -1) {
            printf("%d ", array[i]);
        }
    }
}

int* make_random_array() {
    static int random[60];
    srand(time(NULL));
    for (int i = 0; i < 60; i++) {
        insert(random, i, rand()%1000);
    }
    return random;
}

int main() {
    int* random_array = make_random_array();

    printf("First Time\n");
    delete(random_array);
    print(random_array);

    printf("\n\nSecond Time\n");
    delete(random_array);
    print(random_array);

    printf("\n\nThird Time\n");
    delete(random_array);
    print(random_array);
}