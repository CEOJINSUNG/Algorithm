N = int(input())

dp = [[0 for _ in range(1024)] for _ in range(10)]

for i in range(1, 10):
    dp[i][1<<i] = 1

for i in range(1, N):
    dp_next = [[0 for _ in range(1024)] for _ in range(10)]
    for j in range(10):
        for k in range(1024):
            if j < 9:
                dp_next[j][k | (1<<j)] = (dp_next[j][k | (1<<j)] + dp[j+1][k]) % 1000000000
            if j > 0 :
                dp_next[j][k | (1<<j)] = (dp_next[j][k | (1<<j)] + dp[j-1][k]) % 1000000000

    
    dp = dp_next

print(sum(dp[i][1023] for i in range(10)) % 1000000000)