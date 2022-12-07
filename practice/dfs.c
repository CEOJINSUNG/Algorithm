#include <stdio.h>

#define VERTICES 11;

int graph[VERTICES][VERTICES];
int visited[VERTICES];

int dfs(int cur) {
    visited[cur] = 1;

    for (int i = 1; i < VERTICES; i++) {
        if (graph[cur][i] == 1 && visited[i] == 0) {
            dfs(i, n);
        }
    }
}

int main() {
    int start = 1;
    graph[1][3] = 1; graph[3][5] = 1; graph[5][7] = 1; 
    graph[3][1] = 1; graph[5][3] = 1; graph[7][5] = 1; 
     
    graph[1][2] = 1; graph[2][4] = 1; graph[4][8] = 1;
    graph[2][1] = 1; graph[4][2] = 1; graph[8][4] = 1;
    
    printf("%d ",start);
    DFS(start); 
    
    return 0;
}