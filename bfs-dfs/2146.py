from collections import deque

n = int(input())
land = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque()
    q.append((x, y))

    coordinate = [(x, y)]
    land[x][y] = 0

    while q:
        x_, y_ = q.popleft()

        for i in range(4):
            new_x = x_ + dx[i]
            new_y = y_ + dy[i]

            if 0 <= new_x < n and 0 <= new_y < n and land[new_x][new_y] == 1:
                land[new_x][new_y] = 0
                q.append((new_x, new_y))
                coordinate.append((new_x, new_y))
    
    return coordinate

island = []

for i in range(n):
    for j in range(n):
        if land[i][j] == 1:
            island.append(bfs(i, j))

answer = 10001
for i in range(len(island)):
    for j in range(i+1, len(island)):
        for x, y in island[i]:
            for new_x, new_y in island[j]:
                answer = min(answer, abs(new_x-x) + abs(new_y-y))

print(answer-1)