from collections import deque
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

degree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
part = [0] * n
middle = set()

for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[x].append([y, k])
    middle.add(x)
    degree[y] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if degree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for next, number in graph[now]:
            degree[next] -= 1

            if degree[next] == 0:
                q.append(next)
            
            if now == n:
                part[next] += number
            else:
                if now in middle:
                    part[next] += (part[now] * number)

topology_sort()

for i in range(1, n):
    if i not in middle:
        print(i, part[i])