import sys

def bfs(x, y, w, h, land):
    dx = [0, 0, -1, 1, 1, -1, 1, -1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]

    q = [(x, y)]

    while q:
        current_x, current_y = q.pop(0)

        for i in range(8):
            new_x, new_y = current_x+dx[i], current_y+dy[i]

            if 0 <= new_x < w and 0 <= new_y < h:
                if land[new_y][new_x] == 1:
                    land[new_y][new_x] = 0
                    q.append((new_x, new_y))
    
    return 1

while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    land = []
    for _ in range(h):
        land.append(list(map(int, sys.stdin.readline().split())))
    
    answer = 0
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1:
                answer += bfs(j, i, w, h, land)
    
    print(answer)