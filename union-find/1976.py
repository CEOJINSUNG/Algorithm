import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(parent[x])
    y = find(parent[y])

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
matrix = []
for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(i, n):
        if row[j] == 1:
            union(i, j+1)
    matrix.append(row)

plans = list(map(int, input().split()))

answer = True
init = find(plans[0])
for i in range(1, m):
    if init != find(plans[i]):
        answer = False
        break
if answer:
    print("YES")
else:
    print("NO")