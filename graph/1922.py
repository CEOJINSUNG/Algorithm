import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
edge = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

edge.sort()

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[y] = x
    else:
        parent[x] = y

cost = 0
for c, a, b in edge:
    if find(a) != find(b):
        cost += c
        union(a, b)

print(cost)