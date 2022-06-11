import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        if cost[parent[x]] > cost[x]:
            cost[parent[x]] = cost[x]
        else:
            cost[x] = cost[parent[x]]
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if cost[a] > cost[b]:
        cost[a] = cost[b]
    else:
        cost[b] = cost[a]

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    v, w = map(int, input().split())
    union(v, w)

answer = 0
possible = set()
for i in range(1, n+1):
    a = find(i)

    if a in possible:
        continue
    else:
        possible.add(a)
        answer += cost[a]

if answer <= k:
    print(answer)
else:
    print("Oh no")