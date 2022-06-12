import sys
input = sys.stdin.readline

electronic = []
num = int(input())
for _ in range(num):
    a, b = map(int, input().split())
    electronic.append((a, b))

electronic.sort()

dp = [1 for _ in range(num)]
for i in range(num):
    for j in range(i):
        if electronic[i][1] > electronic[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(num - max(dp))