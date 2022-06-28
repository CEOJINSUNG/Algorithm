n, q = map(int, input().split())
array = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(2, n+1):
    dp[i] += abs(array[i] - array[i-1]) + dp[i-1]

for _ in range(q):
    a, b = map(int, input().split())
    print(dp[b] - dp[a])