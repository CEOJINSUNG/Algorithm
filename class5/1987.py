from collections import deque

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = 1

def bfs(x, y):
    global answer
    q = deque()
    q.append((x, y, board[x][y]))

    while q:
        x_, y_, alpha_ = q.pop()

        for i in range(4):
            new_x = x_ + dx[i]
            new_y = y_ + dy[i]

            if ((0 <= new_x < R) and (0 <= new_y < C)):
                if board[new_x][new_y] not in alpha_:
                    q.append((new_x, new_y, alpha_ + board[new_x][new_y]))
                    answer = max(answer, len(alpha_) + 1)

bfs(0, 0)
print(answer)