from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

miro = [list(map(int, input().strip())) for _ in range(n)]

visited = [[int(1e9)]*m for _ in range(n)]

q = deque()
q.append((0, 0))
visited[0][0] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    cur_x, cur_y = q.popleft()

    for i in range(4):
        new_x = cur_x + dx[i]
        new_y = cur_y + dy[i]

        if 0 <= new_x < m and 0 <= new_y < n:
            if visited[new_y][new_x] == int(1e9):
                if miro[new_y][new_x] == 0:
                    visited[new_y][new_x] = visited[cur_y][cur_x]
                    q.appendleft((new_x, new_y))
                else:
                    visited[new_y][new_x] = visited[cur_y][cur_x] + 1
                    q.append((new_x, new_y))

print(visited[n-1][m-1])