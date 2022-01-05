from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
def dfs(graph, v):
    print(v, end=' ')
    visited[v] = 1
    for i in sorted(graph[v]):
        if visited[i] != 1:
            dfs(graph, i)

dfs(graph, V)
print()

def bfs(graph, start):
    queue = deque([start])
    visited = []
    visited.append(start)
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return visited

bfs(graph, V)