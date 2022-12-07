#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

// 간선 구조체
struct Edge {
    int src;
    int dest;
    int weight;
};

// 그래프 구조체
struct Graph {
    int V, E;

    struct Edge* edge;
};

// 그래프 초기 생성
struct Graph* createGraph(int V, int E) {
    struct Graph* graph = (struct Graph*) malloc(sizeof(struct Graph));

    graph->V = V;
    graph->E = E;
    graph->edge = (struct Edge*) malloc(graph->E * sizeof(struct Edge));

    return graph;
};

// 벨만 포드 src에서 다른 정점까지의 최단 거리를 찾아주는데 음의 가중치도 적용이 가능하다
void BellmanFord(struct Graph* graph, int src) {
    int V = graph->V;
    int E = graph->E;
    int *dist = (int *)malloc(sizeof(int)*V);

    for (int i = 0; i < V; i++) {
        dist[i] = INT_MAX;
    }
    dist[src] = 0;

    for (int i = 1; i < V; i++) {
        for(int j = 0; j < E; j++) {
            int u = graph->edge[j].src;
            int v = graph->edge[j].dest;
            int weight = graph->edge[j].weight;

            // 정점 시작점이 무한대가 아님
            if(dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
            }
        }
    }

    // 음의 가중치로 무한히 작아지는 경우가 있는지 확인 
    for (int i = 0; i < E; i++) {
        int u = graph->edge[i].src;
        int v = graph->edge[i].dest;
        int weight = graph->edge[i].weight;

        if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
            printf("Graph contains negative weight");
        }
    }  
    return;
}