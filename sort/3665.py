from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    rank = list(map(int,input().split()))

    cntLink = [-1] + [0]*n
    link = [[] for _ in range(n+1)]
    for i in range(n):
        link[rank[i]] = rank[i+1:]
        cntLink[rank[i]] = i
    
    for _ in range(int(input())):
        a,b = map(int,input().split())
        if a in link[b]:
            link[b].remove(a)
            link[a].append(b)
            cntLink[a] -= 1
            cntLink[b] += 1
        else:
            link[a].remove(b)
            link[b].append(a)
            cntLink[b] -= 1
            cntLink[a] += 1
    
    q = deque()
    for i in range(1,n+1):
        if not cntLink[i]:
            q.append(i)
    if not q:
        print("IMPOSSIBLE")
        continue
    
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for i in link[v]:
            cntLink[i] -= 1
            if not cntLink[i]:
                q.append(i)
    if sum(cntLink) > -1:
        print("IMPOSSIBLE")
    else:
        print(*ans)
