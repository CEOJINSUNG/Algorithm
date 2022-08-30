from collections import deque
import sys
input = sys.stdin.readline

miro = [list(input().strip()) for _ in range(8)]
visited =[[False] * 8 for _ in range(8)]

dx = [0, 0, 1, -1, 1, -1, 1, -1, 0]
dy = [1, -1, 0, 0, 1, 1, -1, -1, 0]

q = deque()
q.append((7, 0))
visited[7][0] = True

answer = 0
while q:
    x, y = q.popleft()

    if miro[x][y] == '#':
        continue

    for i in range(9):
        new_x, new_y = x + dx[i], y + dy[i]

        if 0 <= new_x < 8 and 0 <= new_y < 8 and miro[new_x][new_y] == "." and not visited[new_x-1][new_y]:
            visited[new_x-1][new_y] = True
            q.append((new_x-1, new_y))

            if new_x == 0:
                answer = 1

print(answer)