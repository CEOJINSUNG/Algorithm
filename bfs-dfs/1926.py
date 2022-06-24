from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0
max_width = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            count += 1
            board[i][j] = 0
            width = 1
            
            q = deque()
            q.append((j, i))

            while q:
                cur_x, cur_y = q.popleft()

                for k in range(4):
                    new_x, new_y = cur_x + dx[k], cur_y + dy[k]

                    if 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] == 1:
                        board[new_y][new_x] = 0
                        width += 1
                        q.append((new_x, new_y))
            
            if width > max_width:
                max_width = width

print(count)
print(max_width)