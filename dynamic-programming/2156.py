import sys
input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]

dp = [0] * n
dp[0] = array[0]

if n > 1:
    dp[1] = array[1] + array[0]

if n > 2:
    dp[2] = max(array[2] + array[1], array[2] + array[0], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-2] + array[i], dp[i-3] + array[i-1] + array[i], dp[i-1])

print(max(dp))