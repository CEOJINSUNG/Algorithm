from collections import deque
import sys
input = sys.stdin.readline

a, b, n, m = map(int, input().split())
s = [0]*100001
visited = [0]*1000001
visited[n] = 1

def bfs(n):
    q = deque()
    q.append(n)

    d = [1, -1, a, -a, b, -b, a, b]

    while q:
        x = q.popleft()

        for i in range(8):
            if i < 6:
                nx = x + d[i]
                if 0 <= nx <= 100000 and visited[nx] == 0:
                    q.append(nx)
                    visited[nx] = 1
                    s[nx] = s[x] + 1
            else:
                nx = x * d[i]
                if 0 <= nx <= 100000 and visited[nx] == 0:
                    q.append(nx)
                    visited[nx] = 1
                    s[nx] = s[x] + 1

bfs(n)
print(s[m])