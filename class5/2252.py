from collections import deque

# 위상정렬 알고리즘을 적용
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
result = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

q = deque()
for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    result.append(node)
    for i in graph[node]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)

print(*result)