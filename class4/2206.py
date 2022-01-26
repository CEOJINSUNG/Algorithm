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

# 위는 시간초과



import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = 0


def bfs():
    # (0, 0) 출발, 벽 안부순 상태 시작
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        r, c, wall = q.popleft()
        if r == N - 1 and c == M - 1:
            return visited[r][c][wall]

        for i in range(4):
            nr = r + dir[i][0]
            nc = c + dir[i][1]
            # 맵 범위 안에 있고, 한 번도 방문하지 않았으면
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][wall] == 0:
                # 벽이 아니라면 이동하고, 이전경로 + 1 visited 배열에 저장
                if board[nr][nc] == 0:
                    q.append((nr, nc, wall))
                    visited[nr][nc][wall] = visited[r][c][wall] + 1
                
                # 벽 1번도 안 부쉈고, 다음 이동할 곳이 벽이라면
                if wall == 0 and board[nr][nc] == 1:
                    # 벽을 부순 상태를 1로 표현
                    q.append((nr, nc, 1))
                    # 벽 부순 상태의 visited[nr][nc][1]에 이전경로 + 1 저장
                    visited[nr][nc][1] = visited[r][c][wall] + 1

    return -1


print(bfs())
