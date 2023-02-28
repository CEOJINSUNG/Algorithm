from collections import deque

n, m = map(int, input().split())
shark = deque()
board = []

for y in range(n):
    row = list(map(int, input().split()))
    for x in range(m):
        if row[x] == 1:
            shark.append((x, y))
    board.append(row)

dx, dy = [0, 0, 1, -1, 1, 1, -1, -1], [1, -1, 0, 0, 1, -1, 1, -1]
answer = 0

while shark:
    cur_x, cur_y = shark.popleft()

    for i in range(8):
        new_x = cur_x + dx[i]
        new_y = cur_y + dy[i]

        if 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] == 0:
            board[new_y][new_x] = board[cur_y][cur_x] + 1
            shark.append((new_x, new_y))
            answer = max(answer, board[cur_y][cur_x] + 1)

print(answer - 1)