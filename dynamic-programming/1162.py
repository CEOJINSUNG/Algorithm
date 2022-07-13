import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

n, m, k = map(int, input().split())
road = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    road[a].append((cost, b))
    road[b].append((cost, a))

dist = [[INF for _ in range(k+1)] for _ in range(n+1)]
dist[1][0] = 0

path = []
heapq.heappush(path, (0, 1, 0))

while path:
    distance, node, count = heapq.heappop(path)

    if dist[node][count] < distance:
        continue

    for next_cost, next_node in road[node]:
        new_cost = distance + next_cost
        if dist[next_node][count] > new_cost:
            dist[next_node][count] = new_cost
            heapq.heappush(path, (new_cost, next_node, count))

        if count < k and dist[next_node][count+1] > distance:
            dist[next_node][count+1] = distance
            heapq.heappush(path, (distance, next_node, count+1))

print(min(dist[n]))