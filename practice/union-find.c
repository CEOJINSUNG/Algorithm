#include <stdio.h>

int findParent(int[] parent, int x) {
    if (parent[x] != x) {
        parent[x] = findParent(parent, parent[x])
    }
    return parent[x]
}

int unionParent(int parent[], int a, int b) {
    a = findParent(parent, a);
    b = findParent(parent, b);

    if (a < b) {
        parent[b] = a;
    } else {
        parent[a] = b;
    }
}

int main(void) {
    int parent[8];
    
    for (int i = 1; i < 8; i++) {
        parent[i] = i;
    }
}