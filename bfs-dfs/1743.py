from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
floor = [[0]*m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    floor[r-1][c-1] = 1

answer = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if floor[i][j] == 1:
            width = 1
            floor[i][j] = 0
            q = deque()
            q.append((j, i))

            while q:
                cur_x, cur_y = q.popleft()

                for p in range(4):
                    new_x, new_y = cur_x + dx[p], cur_y + dy[p]

                    if 0 <= new_x < m and 0 <= new_y < n and floor[new_y][new_x] == 1:
                        q.append((new_x, new_y))
                        width += 1
                        floor[new_y][new_x] = 0

            answer = max(answer, width)

print(answer)