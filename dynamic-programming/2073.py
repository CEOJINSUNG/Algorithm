import sys

d, p = map(int, sys.stdin.readline().split())
l = []
c = []

for _ in range(p):
    length, capacity = map(int, sys.stdin.readline().split())
    l.append(length)
    c.append(capacity)

dp = [0 for _ in range(d+1)]
dp[0] = int(1<<24)
for i in range(p):
    for j in range(d, 0, -1):
        if j >= l[i]:
            dp[j] = max(dp[j], min(dp[j-l[i]], c[i]))

print(dp[d])

# dp = [[0]*(d+1) for _ in range(p+1)]
# component = [[""] * (d+1) for _ in range(p+1)]

# for i in range(1, p+1):
#     for j in range(1, d+1):
#         if j >= l[i]:
#             if dp[i-1][j-l[i]] + c[i] >= dp[i-1][j]:
#                 component[i][j] = str(c[i]) + " " + component[i-1][j-l[i]] 
#             else:
#                 component[i][j] = component[i-1][j]
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-l[i]] + c[i])
#         else:
#             dp[i][j] = dp[i-1][j]
#             component[i][j] = component[i-1][j]

# print(sorted(list(component[p][d].split()))[0])