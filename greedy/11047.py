import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))

answer = 0
for i in range(n-1, -1, -1):
    if coin[i] <= k:
        answer += (k // coin[i])
        k = k % coin[i]

print(answer)