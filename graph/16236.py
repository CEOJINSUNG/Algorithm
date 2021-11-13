# 공간의 크기 입력받기
n = int(input())

# 공간 선언
n_n = []

# 아기 상어 위치 (x, y)와 baby_shark[0]은 아기상어의 크기
baby_shark = [2]

# 입력받은 물고기와 아기 상어 위치 넣기
for i in range(n):
    fish_shark = list(map(int, input().split()))

    # 아기 상어의 위치 파악하기
    if 9 in fish_shark:
        baby_shark.append(fish_shark.index(9))
        baby_shark.append(i)
    n_n.append(fish_shark)

# 갈수 있는 곳인지 아닌지 판단하는 함수
def can_go_or_not(x, y):
    # 아기 상어가 공간을 벗어날 경우 False 반환
    if x >= n or y >= n:
        return False
    # 아기상어의 크기가 가고자 하는 크기보다 작을 경우 False
    if n_n[y][x] > baby_shark[0]:
        return False
    # 방문했던 곳이라면 False

# bfs 선언
def bfs(x, y):
    # 상하좌우에 필요한 좌표
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    # 초기 넓이 선언
    initial_width = 0

    # 큐 선언
    q = []

    # 초기 좌표 삽입
    q.append((x, y))

    # 초기 좌표 방문한 것으로 바꾸고 넓이 더함
    n_n[y][x] = 1

    while q:
        x_, y_ = q.pop(0)

        for i in range(4):
            new_x_ = x_ + dx[i]
            new_y_ = y_ + dy[i]
            if 0 <= new_x_ < n and 0 <= new_y_ < n and n_n[new_y_][new_x_] <= baby_shark[0]:
                n_n[new_y_][new_x_] = 1
                initial_width += 1
                q.append((new_x_, new_y_))
    
    return initial_width

