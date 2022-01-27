import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
hour = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
q = deque()
q.append((0, 0))

while True:
    next_q = deque()
    stop = True

    while q:
        x_, y_ = q.popleft()
        for i in range(4):
            new_x = x_ + dx[i]
            new_y = y_ + dy[i]

            if 0 <= new_x < M and 0 <= new_y < N:
                if cheese[new_y][new_x] == 0:
                    cheese[new_y][new_x] = -1
                    q.append((new_x, new_y))
                elif cheese[new_y][new_x] > 0:
                    stop = False
                    cheese[new_y][new_x] += 1
                    if cheese[new_y][new_x] > 2:
                        next_q.append((new_x, new_y))
                        cheese[new_y][new_x] = -1

    q = next_q
    if stop:
        break

    hour += 1


print(hour)