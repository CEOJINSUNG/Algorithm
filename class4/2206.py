import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
wall = [list(map(int, input().rstrip())) for _ in range(N)]

def bfs():
    q = []
    q.append((0, 0, 1))
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1

    while q:
        x, y, w = q.pop(0)
        if x == N-1 and y == M-1:
            return visited[x][y][w]
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < N and 0 <= new_y < M:
                if wall[new_x][new_y] == 1 and w == 1:
                    visited[new_x][new_y][0] = visited[x][y][1] + 1
                    q.append((new_x, new_y, 0))
                elif wall[new_x][new_y] == 0 and visited[new_x][new_y][w] == 0:
                    visited[new_x][new_y][w] = visited[x][y][w] + 1
                    q.append((new_x, new_y, w))
    
    return -1

print(bfs())