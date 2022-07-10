a, b, d, N = map(int, input().split())

answer, sum = 1, 0
dp = [0]*(N+1)
dp[0] = 1
for i in range(1, N+1):
    if i >= b: 
        sum -= dp[i-b] - 1000
        sum %= 1000
    if i >= a:
        sum += dp[i-a]
        sum %= 1000
    dp[i] = sum
    answer += dp[i]
    if i >= d: 
        answer -= dp[i-d] - 1000
        sum %= 1000

print(answer%1000)