#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 15
 
typedef struct Queue {
    int front, rear;
    int *data;
}Queue;
 
int size, inDegree[MAX_SIZE];
int node[MAX_SIZE][MAX_SIZE];
 
void EnQ(Queue * q, int data) {
    if(q->front == (q->rear + 1)) //FullQ
    {
        puts("Queue is Full");
        return;
    }
    else
    {
        q->rear = q->rear + 1;
        q->data[q->rear] = data;
    }
    return;
}
int DeQ(Queue * q) {
    if(q->front == q->rear) //EmptyQ
    {
        puts("Queue is Empty");
        return;
    }
    else
    {
        q->front = q->front + 1;
        return q->data[q->front];
    }
}

void topology() {
    int result[MAX_SIZE];
    Queue q;
    q.front = 0;
    q.rear = 0;
    q.data = malloc(sizeof(int)*MAX_SIZE);

    for (int i = 1; i <= size; i++) {
        if (inDegree[i] == 0) {
            EnQ(&q, i);
        }
    }

    for (int i = 1; i <= size; i++) {
        if (q.front == q.rear) {
            printf("사이클이 발생하였습니다.")
            return;
        }

        int x = DeQ(&q);
        int count = 0;
        result[i] = x;

        for (int y = 1; y <= size; y++) {
            if (node[x][y] == 1) {
                node[x][y] = 0;
                if (--inDegree[y] == 0) {
                    EnQ(&q, y);
                }
            }
        }
    }
}