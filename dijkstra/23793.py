from collections import defaultdict
import heapq
import sys

INF = sys.maxsize

n, m = map(int, sys.stdin.readline().split())
graph = {i: defaultdict(dict) for i in range(1, n+1)}

for _ in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start][end] = weight

x, y, z = map(int, sys.stdin.readline().split())

def dijkstra(start, middle, end, wi):
    distances = {i: INF for i in range(1, n+1)}
    distances[start] = 0

    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, node = heapq.heappop(queue)

        if distances[node] < current_distance: continue

        for adjacency, distance in graph[node].items():
            if wi == False and adjacency == middle:
                continue

            weighted_distance = current_distance + distance
            if weighted_distance < distances[adjacency]:
                distances[adjacency] = weighted_distance
                heapq.heappush(queue, (weighted_distance, adjacency))

    return distances

x_to_y = dijkstra(x, 0, y, True)[y]
y_to_z = dijkstra(y, 0, z, True)[z]
x_to_z = dijkstra(x, y, z, False)[z]

if x_to_y != INF and y_to_z != INF:
    print(x_to_y + y_to_z, end = " ")
else:
    print(-1, end = " ")

if x_to_z != INF:
    print(x_to_z)
else:
    print(-1)