from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x_, y_ = q.popleft()
        
        for i in range(4):
            new_x = x_ + dx[i]
            new_y = y_ + dy[i]

            if 0 <= new_x < M and 0 <= new_y < N and matrix[new_y][new_x] == 0 and visited[new_y][new_x]:
                q.append((new_x, new_y))
                visited[new_y][new_x] = True
