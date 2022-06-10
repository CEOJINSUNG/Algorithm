import sys
input = sys.stdin.readline

n, k = map(int, input().split())
value = []
for _ in range(n):
    value.append(int(input()))

dp = [0]*(k+1)
dp[0] = 1
for i in range(n):
    for j in range(value[i], k+1):
        if dp[j-value[i]] > 0:
            dp[j] += dp[j-value[i]]

print(dp[k])