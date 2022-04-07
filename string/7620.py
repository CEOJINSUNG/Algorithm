n = input()
m = input()

def dist(str1, str2):
    dp = [[0] for _ in range(len(str2) + 1) for _ in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        dp[i][0] = i
    
    for j in range(1, len(str2) + 1):
        dp[0][j] = j
    
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[j][i-1]) + 1
    
    return dp[-1][-1]

print(dist(n, m))