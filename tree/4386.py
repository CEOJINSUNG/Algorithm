import sys, math
input = sys.stdin.readline

n = int(input())
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

coordinate = []
for i in range(1, n+1):
    x, y = map(float, input().split())
    coordinate.append([x, y])

edges = []
for i in range(n-1):
    for j in range(i+1, n):
        edges.append((math.sqrt((coordinate[i][0] - coordinate[j][0])**2 + (coordinate[i][1] - coordinate[j][1])**2), i, j))

edges.sort()
answer = 0
for edge in edges:
    cost, x, y = edge
    if find(x) != find(y):
        union(x, y)
        answer += cost

print(round(answer, 2))