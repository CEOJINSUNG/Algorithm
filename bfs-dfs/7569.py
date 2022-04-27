from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())

tomato_box = []
q = deque()

for height in range(h):
    each_floor = []
    for column in range(n):
        each_floor.append(list(map(int, sys.stdin.readline().split())))
        for row in range(m):
            if each_floor[column][row] == 1:
                q.append((column, row, height))
    tomato_box.append(each_floor)

def bfs():
    global q
    d_column = [0, 0, 0, 0, -1, 1]
    d_row = [0, 0, -1, 1, 0, 0]
    d_height = [-1, 1, 0, 0, 0, 0]

    while q:
        current_column, current_row, current_height = q.popleft()

        for i in range(6):
            new_column, new_row, new_height = current_column + d_column[i], current_row + d_row[i], current_height + d_height[i]

            if 0 <= new_column < n and 0 <= new_row < m and 0 <= new_height < h:
                if tomato_box[new_height][new_column][new_row] == 0:
                    tomato_box[new_height][new_column][new_row] = tomato_box[current_height][current_column][current_row] + 1
                    q.append((new_column, new_row, new_height))

bfs()

zero_exist = False
max_day = 0
for height in range(h):
    for column in range(n):
        row = tomato_box[height][column]
        if 0 in row:
            zero_exist = True
            break

        max_day = max(max_day, max(row))
    if zero_exist:
        break

if zero_exist:
    print(-1)
else:
    print(max_day-1)