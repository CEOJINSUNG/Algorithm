import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

path = {i: [] for i in range(1, N+1)}
dist = {i: INF for i in range(1, N+1)}

for _ in range(M):
    start, end, weight = map(int, input().split())
    path[start].append((weight, end))

def dijkstra(start):
    dist[start] = 0

    queue = []
    heapq.heappush(queue, [dist[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        
        if dist[current_destination] < current_distance:
            continue
        
        for new_distance, new_destination in path[current_destination]:
            distance = dist[current_destination] + new_distance
            if distance < dist[new_destination]:
                dist[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

start, end = map(int, input().split())

dijkstra(start)

print(dist[end])