import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    nation = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        nation[a].append(b)
        nation[b].append(a)
    
    print(n-1)
