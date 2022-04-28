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
middle = list(map(int, sys.stdin.readline().split()))

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

length = len(middle)

answer = INF
for i in range(length):
    for j in range(length):
        for k in range(length):
            if i != j and j != k and i != k:
                result_start = dijkstra(middle[i])
                result_end = dijkstra(middle[j])
                result = result_start[x] + result_end[z] + result_start[middle[k]] + result_end[middle[k]]
                answer = min(answer, result)

print(answer)