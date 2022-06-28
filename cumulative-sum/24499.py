n, k = map(int, input().split())
array = list(map(int, input().split()))

dp = [0]*2*n
temp = array + array

dp[0] = array[0]
for i in range(1, k):
    dp[i] = dp[i-1] + temp[i]

answer = 0
for i in range(k, 2*n):
    dp[i] = dp[i-1] - temp[i-k] + temp[i]
    answer = max(answer, dp[i])

print(answer)