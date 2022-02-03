import sys

N, M = map(int, sys.stdin.readline().split())
memory = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
max_cost = sum(cost)

def app(n, m, mem, co):
    global max_cost
    dp = [[0 for _ in range(sum(co)+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(len(dp[0])):
            if co[i] > j: 
                dp[i][j] = dp[i - 1][j] 
            else: 
                dp[i][j] = max(dp[i - 1][j - co[i]] + mem[i], dp[i - 1][j]) 
            
            if dp[i][j] >= m:
                max_cost = min(max_cost, j)
    
    return max_cost

print(app(N, M, memory, cost))