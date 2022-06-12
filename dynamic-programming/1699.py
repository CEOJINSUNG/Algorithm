n = int(input())

dp = [0 for _ in range(n+1)]
square = [i*i for i in range(1, n+1)]

for i in range(1, n+1):
    array = []
    for j in square:
        if j > i:
            break
        array.append(dp[i-j])
    dp[i] = min(array) + 1
print(dp[n])