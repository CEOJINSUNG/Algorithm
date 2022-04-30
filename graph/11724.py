import sys

n, m = map(int, sys.stdin.readline().split())
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

component = set()
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    
    if find(a) != find(b):
        union(a, b)

for i in range(1, n+1):
    component.add(find(i))

print(len(component))