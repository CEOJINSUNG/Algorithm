from collections import deque

N, M = map(int, input().split())

degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
    degree[a] += 1

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, N+1):
        if degree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(i)

        for i in graph[current]:
            degree[i] -= 1
            if degree[i] == 0:
                queue.append(i)
    return result

is_cycle = topology_sort()
print(is_cycle, len(is_cycle))