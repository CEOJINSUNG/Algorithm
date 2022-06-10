from collections import deque
import sys

n = int(sys.stdin.readline())
color = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

first = [[False]*n for _ in range(n)]
second = [[False]*n for _ in range(n)]

def bfs(x, y, visited):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque()
    q.append((x, y))
    visited[y][x] = True
    current = color[y][x]

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            new_x, new_y = cur_x + dx[i], cur_y + dy[i]

            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_y][new_x] and color[new_y][new_x] == current:
                 q.append((new_x, new_y))
                 visited[new_y][new_x] = True
    
    return 1

one = 0
for i in range(n):
    for j in range(n):
        if not first[i][j]:
            one += bfs(j, i, first)
                
print(one, end=" ")

def bfs_two(x, y, visited):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque()
    q.append((x, y))
    visited[y][x] = True
    current = color[y][x]

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            new_x, new_y = cur_x + dx[i], cur_y + dy[i]

            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_y][new_x]:
                next = color[new_y][new_x]
                if (current == "R" or current == "G") and (next == "R" or next == "G"):
                    q.append((new_x, new_y))
                    visited[new_y][new_x] = True
                elif current == "B" and next == current:
                    q.append((new_x, new_y))
                    visited[new_y][new_x] = True
    
    return 1

two = 0
for i in range(n):
    for j in range(n):
        if not second[i][j]:
            two += bfs_two(j, i, second)
                
print(two)