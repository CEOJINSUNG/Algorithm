import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (n+1)
dp = [[0, 0] for _ in range(n+1)]

def dfs(start):
    visited[start] = True
    dp[start][0] = 1

    for i in tree[start]:
        if not visited[i]:
            dfs(i)
            dp[start][0] += min(dp[i][0], dp[i][1])
            dp[start][1] += dp[i][0]

dfs(1)
print(min(dp[1][0], dp[1][1]))