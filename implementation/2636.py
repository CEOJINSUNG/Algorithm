from collections import deque
import sys

input = sys.stdin.readline

vertical, horizontal = map(int, input().split())
cheese = []
for _ in range(vertical):
    row = list(map(int, input().split()))
    cheese.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = []

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    time = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < vertical and 0 <= ny < horizontal and visited[nx][ny] == False:
                if cheese[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif cheese[nx][ny] == 1:
                    cheese[nx][ny] = 0
                    visited[nx][ny] = True
                    time += 1
    count.append(time)
    return time

hour = 0
while 1:
    hour += 1
    visited = [[False]*horizontal for _ in range(vertical)]

    if bfs() == 0:
        break

print(hour-1)
print(count[-2])