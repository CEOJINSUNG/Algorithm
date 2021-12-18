import heapq
import math

v, e = map(int, input().split())

k = int(input())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start, distance):
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

INF = float('inf')

distances = [INF] * (v+1)

dijkstra(start=k, distance=distances)

for i in range(1, v+1):
    if math.isinf(distances[i]):
        print("INF")
    else:
        print(distances[i])