import sys

r, c = map(int, sys.stdin.readline().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]

dx = [-1, 0, 1]
answer = 0

def dfs(i, j):
    if j == c-1:
        return True
    
    for k in dx:
        new_i = i+k
        if 0 <= new_i < r and graph[new_i][j+1] == '.' and not visited[new_i][j+1]:
            visited[new_i][j+1] = True
            if dfs(new_i, j+1):
                return True
    return False

for i in range(r):
    if graph[i][0] == '.':
        if dfs(i, 0):
            answer += 1

print(answer)