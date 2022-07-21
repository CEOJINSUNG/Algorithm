from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)

def bfs(start):
    cnt = 0
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    queue = deque([[start, 0]])
    while queue:
        u, dist = queue.popleft()
        if dist <= 2:
            cnt += 1
        for v in graph[u]:
            if not visited[v]:
                visited[v] = 1
                queue.append([v, dist+1])
    return cnt-1

print(bfs(1))