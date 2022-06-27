import sys
input = sys.stdin.readline

n, m = map(int, input().split())
school = [""] + list(map(str, input().split()))
edges = []
for _ in range(m):
    u, v, d = map(int, input().split())
    if school[u] != school[v]:
        edges.append((d, u, v))

edges.sort()

parent = [i for i in range(n+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

answer, road = 0, 0
for edge in edges:
    d, u, v = edge
    if find(u) != find(v):
        union(u, v)
        answer += d
        road += 1
    if road == n-1:
        break

print(answer if road == n-1 else -1)