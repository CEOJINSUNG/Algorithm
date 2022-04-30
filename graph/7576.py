import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

tomato = []
position = deque()

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    tomato.append(row)

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            position.append((j, i))

answer = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while position:
    current_x, current_y = position.popleft()

    for i in range(4):
        new_x, new_y = current_x + dx[i], current_y + dy[i]

        if 0 <= new_x < m and 0 <= new_y < n and tomato[new_y][new_x] == 0:
            tomato[new_y][new_x] = tomato[current_y][current_x] + 1
            position.append((new_x, new_y))

for row in tomato:
    if 0 in set(row):
        print(-1)
        exit(0)
    answer = max(answer, max(row))

print(answer-1)