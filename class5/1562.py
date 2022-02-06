N = int(input())

dp = [0] * 101
dp[10] = 1

if N <= 10:
    print(dp[N])
else:
    for i in range(11, N+1):
        dp[i] = dp[i-1] * 2

    print(dp[N])