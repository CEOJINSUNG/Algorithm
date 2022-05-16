import sys
import heapq
INF = sys.maxsize

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])

def dijsktra(start):
    distances = [INF for _ in range(n+1)]
    distances[start] = 0

    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost+next_cost, next_node])
    return distances

distances = dijsktra(2)

def rational_path(cur_node):
    if dp[cur_node] == 0:
        for next_node, next_cost in nodes[cur_node]:
            if distances[cur_node] > distances[next_node]:
                dp[cur_node] += rational_path(next_node)
        return dp[cur_node]
    else:
        return dp[cur_node]


dp = [0 for _ in range(n+1)]
dp[2] = 1

print(rational_path(1))