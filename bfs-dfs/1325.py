from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trust = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    trust[b].append(a)

standard, answer = 0, []
for i in range(1, n+1):
    visited = [False]*(n+1)
    visited[i] = True

    q = deque([i])

    count = 0
    while q:
        node = q.popleft()
        for next in trust[node]:
            if not visited[next]:
                visited[next] = True
                count += 1
                q.append(next)
    
    if count > standard:
        standard = count
        answer = [i]
    elif count == standard:
        answer.append(i)

print(*answer)