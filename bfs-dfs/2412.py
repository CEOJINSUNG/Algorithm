from collections import deque
import sys
input = sys.stdin.readline

n, T = map(int, input().split())

coordinate = []
max_x = 0
for _ in range(n):
    x, y = map(int, input().split())
    max_x = max(max_x, x)
    coordinate.append((x, y))

mountain = [[0]*(max_x+1) for _ in range(T+1)]
for x, y in coordinate:
    mountain[y][x] = 1

dx = [-2, -1, 0, 1, 2]
dy = [-2, -1, 0, 1, 2]

q = deque()
q.append((0, 0, 0))

answer = -1
exist = False
while q:
    cur_x, cur_y, cur_count = q.popleft()

    if cur_y == T:
        answer = cur_count
        break

    for i in range(5):
        for j in range(5):
            new_x, new_y = cur_x + dx[i], cur_y + dy[j]

            if 0 <= new_x < max_x+1 and 0 <= new_y < T+1 and mountain[new_y][new_x] == 1:
                if new_y == T:
                    answer = cur_count + 1
                    print(answer)
                    exit()
                mountain[new_y][new_x] = 0
                q.append((new_x, new_y, cur_count + 1))

print(answer)