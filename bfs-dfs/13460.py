# n, m = map(int, input().split())

# board = []
# r = (0, 0)
# b = (0, 0)
# o = (0, 0)

# for i in range(n):
#     row = list(input())
#     board.append(row)

#     if 'R' in row:
#         r = (row.index('R'), i)
    
#     if 'B' in row:
#         b = (row.index('B'), i)
    
#     if 'O' in row:
#         o = (row.index('O'), i)

# print(r, b, o)

# # arrow will include up: 0, down: 1, right: 2, left: 3
# arrow = []

# # x means horizontal and y means vertical in sequence up, down, right, left
# dx = [0, 0, 1, -1]
# dy = [-1, 1, 0, 0]

# def bfs(x, y, graph):
#     q = []
#     q.append([(x, y)])

#     while q:
#         path = q.pop(0)
#         graph[y][x] = 0

#         current_x, current_y = path[-1]

#         if graph[current_y][current_x] == 'O':
#             previous_x, previous_y = path[-2]
#             graph[current_y][current_x] = graph[previous_y][previous_x]
#             for k in range(len(graph)):
#                 print(*graph[k])
#             return path
        
#         for i in range(4):
#             next_x, next_y = current_x + dx[i], current_y + dy[i]

#             if 0 < next_x < m-1 and 0 < next_y < n-1 and (graph[next_y][next_x] == "." or graph[next_y][next_x] == "B" or graph[next_y][next_x] == "O"):
#                 if graph[next_y][next_x] == 'O':
#                     graph[next_y][next_x] = "O"
#                 # elif graph[next_y][next_x] != 'O':
#                 #     graph[next_y][next_x] = "#"
#                 elif len(arrow) == 0:
#                     #push the way of marble
#                     arrow.append(i)
                        
#                     # Change the Basic position to 1
#                     # . -> 1
#                     graph[next_y][next_x] = 1
                
#                 # if previous way is the same as current way, maintain it
#                 elif arrow[-1] == i:
#                     graph[next_y][next_x] = graph[current_y][current_x]
                
#                 # if previous way is diffrent from current way, increase the number of way
#                 elif arrow[-1] != i:
#                     graph[next_y][next_x] = graph[current_y][current_x] + 1
#                     arrow.append(i)
                
#                 new_path = list(path)
#                 new_path.append((next_x, next_y))
#                 q.append(new_path)
    
#     return -1

# print(bfs(r[0], r[1], board))

# print(arrow)

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [list(stdin.readline()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            graph[i][j] = '.'
            red = [i, j]
        elif graph[i][j] == 'B':
            graph[i][j] = '.'
            blue = [i, j]


def movemove(x, y, dx, dy):
    move = 0
    while graph[x+dx][y+dy] != '#':
        # 구멍으로 탈출할 경우 0,0 return
        if graph[x+dx][y+dy] == 'O':
            return 0, 0, 0
        x += dx
        y += dy
        move += 1
    return x, y, move


def bfs():
    # 빨간 구슬과 파란 구슬 동시에 방문체크 해야함
    visit = {}
    queue = deque([red + blue])
    visit[red[0], red[1], blue[0], blue[1]] = 0
    while queue:
        rx, ry, bx, by = queue.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):      # 상하좌우
            nrx, nry, rmove = movemove(rx, ry, dx, dy)
            nbx, nby, bmove = movemove(bx, by, dx, dy)
            # 두 공 모두 또는 파란 공만 탈출한 경우
            if not nbx and not nby:
                continue
            # 빨간 공만 탈출한 경우
            elif not nrx and not nry:
                print(visit[rx, ry, bx, by] + 1)
                return
            # 두 공이 같은 위치에 있는 경우
            elif nrx == nbx and nry == nby:
                # 이동거리가 적은 구슬을 한 칸 뒤로
                if rmove > bmove:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
            # visit하지 않았으면 queue에 append
            if (nrx, nry, nbx, nby) not in visit:
                visit[nrx, nry, nbx, nby] = visit[rx, ry, bx, by] + 1
                queue.append([nrx, nry, nbx, nby])
        # answer에 값을 넣었거나 queue가 비었거나 움직인 횟수가 10이상이면 그만
        if not queue or visit[rx, ry, bx, by] >= 10:
            print(-1)
            return


bfs()