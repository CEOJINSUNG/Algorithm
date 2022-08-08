import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    file = list(map(int, input().split()))

    dp = [[0]*(k+1) for _ in range(k+1)]
    for i in range(k-1):
        dp[i][i+1] = file[i] + file[i+1]
        for j in range(i+2, k):
            dp[i][j] = dp[i][j-1] + file[j]
    
    for x in range(2, k):
        for y in range(k-x):
            z = x + y
            dp[y][z] += min([dp[y][a] + dp[a+1][z] for a in range(y, z)])
    
    print(dp[0][k-1])