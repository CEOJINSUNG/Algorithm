import sys

n, k = map(int, sys.stdin.readline().split())
w = []
v = []
dp = [0 for _ in range(k+1)]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    w.append(a)
    v.append(b)

for i in range(n):
    for j in range(k, 0, -1):
        if j >= w[i]:
            dp[j] = max(dp[j-w[i]] + v[i], dp[j])

print(dp[k])