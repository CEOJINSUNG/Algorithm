import heapq
import sys

INF = sys.maxsize

n, m = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

x, z = map(int, sys.stdin.readline().split())
p = int(sys.stdin.readline())
middle = set(list(map(int, sys.stdin.readline().split())))

def dijkstra(start):
    distance = {i: INF for i in range(1, n+1)}
    distance[start] = 0

    q = []
    heapq.heappush(q, (distance[start], start))

    while q:
        current_distance, current_node = heapq.heappop(q)

        if distance[current_node] < current_distance: continue

        for next_distance, next_node in graph[current_node]:
            weighted_distance = current_distance + next_distance
            if weighted_distance < distance[next_node]:
                distance[next_node] = weighted_distance
                heapq.heappush(q, (distance[next_node], next_node))
    
    return distance

result_x = dijkstra(x)
result_z = dijkstra(z)

answer = INF
for i in middle:
    answer = min(answer, result_x[i] + result_z[i])

if answer == INF:
    print(-1)
else:
    print(answer)