T = int(input())

def bfs(x, y):
    # 상하좌우에 필요한 좌표
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    # 큐 선언
    q = []

    # 초기 좌표 삽입
    q.append((x, y))

    # 초기 좌표 방문한 것으로 바꾸고 넓이 더함
    area[y][x] = 0

    while q:
        x_, y_ = q.pop(0)

        for i in range(4):
            new_x_ = x_ + dx[i]
            new_y_ = y_ + dy[i]
            if 0 <= new_x_ < M and 0 <= new_y_ < N and area[new_y_][new_x_] == 1:
                area[new_y_][new_x_] = 0
                q.append((new_x_, new_y_))
    
    return 1

for _ in range(T):
    M, N, K = map(int, input().split())

    area = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        m, n = map(int, input().split())
        area[n][m] = 1
    
    larva = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] == 1:
                larva += bfs(j, i)

    print(larva)