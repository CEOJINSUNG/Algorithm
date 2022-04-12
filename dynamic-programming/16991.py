import sys
from math import sqrt
input = sys.stdin.readline
 
INF = 12345678
dp = [[-1 for _ in range(1<<16)] for _ in range(16)]
a = [[0 for _ in range(16)] for _ in range(16)]
b = []
 
def getDist(a1,a2):
    return sqrt((a1[0] - a2[0])*(a1[0] - a2[0]) + (a1[1] - a2[1])*(a1[1] - a2[1]))
 
def f(now, bit):
    if bit == (1<<n)-1:
        if a[now][0]: return a[now][0]
        return INF
    
    if dp[now][bit] != -1: return dp[now][bit]
 
    dp[now][bit] = INF
    for i in range(n):
        if bit&(1<<i)==0 and a[now][i] != 0:
            dp[now][bit] = min(dp[now][bit], f(i, bit|(1<<i)) + a[now][i])
    
    return dp[now][bit]
 
 
n = int(input())
for i in range(n):
    b.append(list(map(int, input().split())))
 
for i in range(n):
    for j in range(n):
        if i==j: continue
        a[i][j] = getDist(b[i], b[j])
 
print(f(0,1))