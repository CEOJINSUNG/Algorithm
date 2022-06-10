import sys
input = sys.stdin.readline

n = int(input())
weight = list(map(int, input().split()))
joy = list(map(int, input().split()))

dp = [0] * (100)

for i in range(n):
    for j in range(99, -1, -1):
        if j >= weight[i]:
            dp[j] = max(dp[j-weight[i]] + joy[i], dp[j])

print(max(dp))