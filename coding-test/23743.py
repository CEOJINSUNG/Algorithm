import heapq

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
total_cost = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    heapq.heappush(edges, (cost, a, b))

warp = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    heapq.heappush(edges, (warp[i], 0, i))

count = 0

while edges:
    cost, a, b = heapq.heappop(edges)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += cost
        count += 1
        if count == n: break

print(total_cost)