n = int(input())

dp = [[0] * (10) for _ in range(n+1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(1, 10):
        dp[i][j] = sum(dp[i-1][j:])

total = 0
for element in dp:
    total += (sum(element)%10007)

print(total % 10007)