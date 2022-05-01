import sys

n, m, k = map(int, sys.stdin.readline().split())

n_list = [0] 

for _ in range(n):
    n_list.append(int(sys.stdin.readline()))
BIT = [0]*(n+1)

def getsum(i):
    s = 0
    while i > 0:
        s += BIT[i]
        i -= (i & (-i))
    return s

def updatebit(i, v):
    while i <= n:
        BIT[i] += v
        i += (i & (-i))

for i, x in enumerate(n_list):
    if i > 0:
        updatebit(i, x)

for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        diff = c - n_list[b]
        updatebit(b, diff)
        n_list[b] = c
    
    if a == 2:
        print(getsum(c) - getsum(b-1))