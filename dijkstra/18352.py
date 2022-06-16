import heapq
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distances = [int(1e9) for _ in range(n+1)]
def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    distances[start] = 0

    result = []
    while h:
        distance, node = heapq.heappop(h)

        if distance > distances[node]:
            continue

        if distance > k:
            continue
        elif distance == k:
            result.append(node)
            continue
        
        for next in graph[node]:
            next_distance = distance + 1
            if next_distance < distances[next]:
                distances[next] = next_distance
                heapq.heappush(h, (next_distance, next))
    return result

array = dijkstra(x)
if len(array) == 0:
    print(-1)
else:
    for i in sorted(array):
        print(i)