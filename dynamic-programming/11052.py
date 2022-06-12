n = int(input())
dp = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(i, n+1):
        dp[j] = max(dp[j], dp[j-i] + dp[i])

print(dp[-1])