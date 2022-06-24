import sys
input = sys.stdin.readline

n, m = map(int, input().split())
friend = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

visited = [False for _ in range(n)]
def dfs(start, num):
    if num == 4:
        print(1)
        exit()
    visited[start] = True

    for node in friend[start]:
        if not visited[node]:
            visited[node] = True
            dfs(node, num+1)
            visited[node] = False

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)