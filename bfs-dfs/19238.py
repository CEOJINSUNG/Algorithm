from collections import deque
import sys
input = sys.stdin.readline

n, m, energy = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]
taxi = list(map(int, input().split()))
customer = [list(map(int, input().split())) for _ in range(m)]

def bfs(tx, ty):
    q = deque()
    q.append((tx, ty))

    visited = [[-1] * n for _ in range(n)]
    visited[tx][ty] = 0

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            new_x, new_y = cur_x + dx[i], cur_y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n and road[new_x][new_y] == 0 and visited[new_x][new_y] == -1:
                q.append((new_x, new_y))
                visited[new_x][new_y] = visited[cur_x][cur_y] + 1
    return visited

def short_distance(visited, customer):
    index = 0
    for sx, sy, ax, ay in customer:
        customer[index].append(visited[sx - 1][sy - 1])
        index += 1
    
    customer.sort(key = lambda x: (-x[4], -x[0], -x[1]))

while customer:
    visited = bfs(taxi[0]-1, taxi[1]-1)
    short_distance(visited, customer)

    sx, sy, ax, ay, taxi_dist = customer.pop()

    for out in customer:
        out.pop()

    visited = bfs(sx-1, sy-1)
    arrive_dist = visited[ax-1][ay-1]
    taxi = [ax, ay]

    if taxi_dist == -1 or arrive_dist == -1:
        energy = -1
        break
    
    energy -= taxi_dist
    if energy < 0:
        break

    energy -= arrive_dist
    if energy < 0:
        break

    energy += arrive_dist * 2

if energy < 0:
    print(-1)
else:
    print(energy)