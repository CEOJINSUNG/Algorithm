import heapq
import math

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (distance[start], start))
    
    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] < dist:
            continue

        for next in graph[node]:
            weighted_distance = dist + next[1]
            if weighted_distance < distance[next[0]]:
                distance[next[0]] = weighted_distance
                heapq.heappush(queue, (weighted_distance, next[0]))
    
    return distance

v1, v2 = map(int, input().split())

INF = float('inf')

one_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

total_path1 = one_dist[v1] + v1_dist[v2] + v2_dist[n]
total_path2 = one_dist[v2] + v2_dist[v1] + v1_dist[n]

final = min(total_path1, total_path2)

if final < INF:
    print(final)
else:
    print(-1)