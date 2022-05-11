from collections import deque
import sys

n = int(sys.stdin.readline())
location = []
max_height = 0

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    max_height = max(max_height, max(row))
    location.append(row)

def bfs(x, y, visited, height):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = deque()
    q.append((x, y))

    visited[y][x] = True

    while q:
        current_x, current_y = q.popleft()

        for i in range(4):
            new_x, new_y = current_x + dx[i], current_y + dy[i]

            if 0 <= new_x < n and 0 <= new_y < n and location[new_y][new_x] > height and visited[new_y][new_x] == False:
                visited[new_y][new_x] = True
                q.append((new_x, new_y))
    
    return 1

answer = 0

for k in range(max_height):
    visited = [[False]*n for _ in range(n)]
    temp = 0
    for i in range(n):
        for j in range(n):
            if location[i][j] > k and visited[i][j] == False:
                temp += bfs(j, i, visited, k)
    
    if answer < temp:
        answer = temp

print(answer)