import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for _ in range(m):
    calculate, x, y = map(int, input().split())

    if calculate == 0:
        union(x, y)
    else:
        root_x = find_parent(x)
        root_y = find_parent(y)

        if root_x == root_y:
            print("YES")
        else:
            print("NO")