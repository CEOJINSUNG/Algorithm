#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
#define MAX_QUEUE_SIZE 10

typedef int element;
typedef struct {
    element queue[MAX_QUEUE_SIZE];
    int front, rear;
} QueueType;

void error(char *message) {
    fprintf("stderr", message);
    exit(1);
}

void queue_init(QueueType *q) {
    q->front = q->rear = 0;
}

int is_empty(QueueType *q) {
    return (q->front == q->rear);
}

int is_full(QueueType *q) {
    return ((q->rear + 1)%MAX_QUEUE_SIZE == q->front);
}

void enqueue(QueueType *q, element item) {
    if(is_full(q)) {
        error("overflow");
    }

    q->rear = (q->rear + 1)%MAX_QUEUE_SIZE;
    q->queue[q->rear] = item;
}

element dequeue(QueueType *q) {
    if (is_empty(q)) {
        error("underflow");
    }

    q->front = (q->front + 1)%MAX_QUEUE_SIZE;
    return q->queue[q->front];
}

#define MAX_VERTICES 50

typedef struct GraphType {
    int n;
    int adj_max[MAX_VERTICES][MAX_VERTICES];
} GraphType;

int visited[MAX_VERTICES];

void graph_init(GraphType* g) {
    int r, c;
    g->n = 0;
    for (r = 0; r < MAX_VERTICES; r++) {
        for (c = 0; c < MAX_VERTICES; c++) {
            g->adj_max[r][c] = 0;
        }
    }
}

void insert_vertex(GraphType* g, int v) {
    if ((g->n) + 1 > MAX_VERTICES) {
        fprintf("stderr", "overflow");
        return;
    }
    g->n++;
}

void insert_edge(GraphType* g, int start, int end) {
    if(start >= g->n || end >= g->n) {
        fprintf("stderr", "graph index error");
        return;
    }
    g->adj_max[start][end] = 1;
    g->adj_max[end][start] = 1;
}

void bfs(GraphType *g, int v) {
    int w;
    QueueType q;

    queue_init(&q);
    enqueue(&q, v);
    visited[v] = TRUE;

    while (!is_empty(&q)) {
        v = dequeue(&q);
        for (w = 0; w < g->n; w++) {
            if (g->adj_max[v][w] && !visited[w]) {
                visited[w] = TRUE;
                enqueue(&q, w);
            }
        }
    }
}

int main(void){
    GraphType *g = (GraphType *)malloc(sizeof(GraphType));
    graph_init(g);
    for(int i=0;i<7;i++)
        insert_vertex(g,i);

    insert_edge(g,0,1);
    insert_edge(g,0,2);
    insert_edge(g,1,3);
    insert_edge(g,1,4);
    insert_edge(g,2,5);
    insert_edge(g,2,6);

    printf("BFS\n");
    bfs_mat(g,0);
    printf("\n");
    free(g);
    return 0;
}