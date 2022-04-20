import sys

n = int(sys.stdin.readline())
paper = []

for _ in range(n):
    width = list(map(int, sys.stdin.readline().split()))
    paper.append(sorted(width))

paper.sort()

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if paper[i][1] >= paper[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))