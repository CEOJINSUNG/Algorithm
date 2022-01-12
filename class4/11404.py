import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

dist = [[float('inf')] * (N) for _ in range(N)]
for _ in range(M):
    a, b, e = map(int, input().split())
    if dist[a-1][b-1] > e:
        dist[a-1][b-1] = e

for k in range(N):
    dist[k][k] = 0
    for i in range(N):
        if k == i:
            continue
        for j in range(N):
            if k == j or i == j:
                continue

            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for rows in dist:
    for element in rows:
        if element == float('inf'):
            print(0, end = " ")
        else:
            print(element, end = " ")
    print()