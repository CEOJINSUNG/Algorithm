import sys
input = sys.stdin.readline

n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, input().split())))

dp = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0:
            if j == 0:
                dp[i][j] = miro[i][j]
            else:
                dp[i][j] = max(dp[i][j-1] + miro[i][j], dp[i][j])
        else:
            if j == 0:
                dp[i][j] = max(dp[i-1][j] + miro[i][j], dp[i][j])
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + miro[i][j], dp[i][j-1] + miro[i][j])

print(dp[n-1][m-1])