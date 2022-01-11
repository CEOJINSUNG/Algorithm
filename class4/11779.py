import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

bus = {i : [] for i in range(1, N+1)}
for _ in range(M):
    start, end, weight = list(map(int, input().split()))
    bus[start].append((weight, end))

def dijkstra(graph, start, destination):
    distances = [float('inf') for _ in range(N+1)]
    queue = [(0, start, [start])]

    while queue:
        weight, end, history = heapq.heappop(queue)

        if end == destination:
            return weight, history

        if distances[end] < weight:
            continue

        for new_weight, new_end in graph[end]:
            distance = weight + new_weight
            if distance < distances[new_end]:
                distances[new_end] = distance
                heapq.heappush(queue, (distance, new_end, history + [new_end]))

city_start, city_end = map(int, input().split())

distance, path = dijkstra(bus, city_start, city_end)
print(distance)
print(len(path))
print(*path)