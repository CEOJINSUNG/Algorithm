from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
link = [[] for _ in range(n+1)]
cntLink = [0]*(n+1)
cost = [0]*(n+1)
for i in range(1,n+1):
    s = list(map(int,input().split()))
    cost[i] = s[0]
    for j in range(1,len(s)-1):
        link[s[j]].append(i)
        cntLink[i] += 1

dp = [0]*(n+1)
q = deque()
for i in range(1,n+1):
    if cntLink[i] == 0:
        q.append(i)
        dp[i] += cost[i]

while q:
    curNode = q.popleft()
    for toNode in link[curNode]:
        cntLink[toNode] -= 1
        dp[toNode] = max(dp[toNode], dp[curNode] + cost[toNode])
        if cntLink[toNode] == 0:
            q.append(toNode)
print(*dp[1:], sep="\n")