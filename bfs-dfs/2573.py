from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

earth = []
for _ in range(n):
    earth.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def shrink(x, y, visited, ice):
    q = deque()
    q.append((x, y))

    visited[y][x] = True
    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if 0 <= next_x < m and 0 <= next_y < n and not visited[next_y][next_x]:
                if earth[next_y][next_x] == 0:
                    visited[next_y][next_x] = True
                    q.append((next_x, next_y))
                elif earth[next_y][next_x] > 0:
                    earth[next_y][next_x] -= 1
                    if earth[next_y][next_x] == 0:
                        ice.append((next_x, next_y))
                        earth[next_y][next_x] = -1

def chunk(x, y, visited):
    q = deque()
    q.append((x, y))

    visited[y][x] = True
    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if 0 <= next_x < m and 0 <= next_y < n and not visited[next_y][next_x]:
                if earth[next_y][next_x] != 0:
                    visited[next_y][next_x] = True
                    q.append((next_x, next_y))
    return 1

year = 1
while True:
    ice = []
    shrink_visit = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not shrink_visit[i][j] and earth[i][j] == 0:
                shrink(j, i, shrink_visit, ice)

    for x, y in ice:
        earth[y][x] = 0

    count = 0
    chunk_visit = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not chunk_visit[i][j] and earth[i][j] != 0:
                count += chunk(j, i, chunk_visit)
    
    if count >= 2:
        print(year)
        break
    elif count == 0:
        print(0)
        break
    year += 1