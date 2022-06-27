import sys
input = sys.stdin.readline

n = int(input())
flow = [list(map(int, input().split())) for _ in range(n)]
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

edges = []
for i in range(n-1):
    for j in range(i+1, n):
        edges.append((flow[i][j], i, j))

edges.sort()
answer = 0
for edge in edges:
    dist, start, end = edge
    if find(start) != find(end):
        union(start, end)
        answer += dist

print(answer)