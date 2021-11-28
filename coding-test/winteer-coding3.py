def solution(cakes, cut_rows, cut_columns):
    # 전체 알파벳 저장 배열 선언
    total_alpha_list = []
    visited = [[0 for _ in range(len(cakes[0]))] for _ in range(len(cakes))]
    for i in range(len(cakes)):
        for j in range(len(cakes[0])):
            if visited[i][j] == 0 and 0 <= j < len(cakes[0]) and 0 <= i < len(cakes):
                total_alpha_list.append(bfs(cakes, visited, cut_rows, cut_columns, j, i))
    return total_alpha_list

# bfs 선언
def bfs(cakes, visited, cut_rows, cut_columns, x, y):
    # 상하좌우에 필요한 좌표
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    # 알파벳 리스트 선언
    alpha_list = []

    # 큐 선언
    q = []

    # 초기 좌표 삽입
    q.append((x, y))

    # 초기 좌표 방문하고 알파벳을 넣어줌
    visited[y][x] = 1
    alpha_list.append(cakes[y][x])
    
    # 가로 길이
    n = len(cakes[0])

    # 세로 길이
    m = len(cakes)
    while q:
        x_, y_ = q.pop(0)

        for i in range(4):
            new_x_ = x_ + dx[i]
            new_y_ = y_ + dy[i]
            cut_standard_x = 0
            cut_standard_y = 0

            if x_ in cut_columns:
                cut_standard_x = x_
            if new_x_ in cut_columns:
                cut_standard_x = new_x_
            
            if y_ in cut_rows:
                cut_standard_y = y_
            if new_y_ in cut_rows:
                cut_standard_y = new_y_
            
            # 조건은 일단 사각형 안에 들어가야 하고 또한 방문하지 않았어야 하고
            if 0 <= new_x_ < n and 0 <= new_y_ < m and visited[new_y_][new_x_] == 0:
                # 둘다 바뀌지 않으면
                if ((cut_standard_x == 0) and (cut_standard_y == 0)):
                    # 방문한 것으로 바꾸고 해당 알파벳을 더함
                    visited[new_y_][new_x_] = 1
                    alpha_list.append(cakes[new_y_][new_x_])
                    q.append((new_x_, new_y_))
                    print("F", alpha_list, new_x_, new_y_)
                # 둘중 하나가 해당이 된다면
                else:
                    x_list = [x_, new_x_]
                    y_list = [y_, new_y_]
                    x_list.sort()
                    y_list.sort()
                    cut_standard_x = abs(cut_standard_x - 0.5)
                    cut_standard_y = abs(cut_standard_y - 0.5)
                    # 기존과 새로 간 곳의 구간 안에 경계 요소가 있다면 pass 함
                    if ((x_list[0] < cut_standard_x) and (x_list[1] > cut_standard_x)) or ((y_list[0] < cut_standard_y) and (y_list[1] > cut_standard_y)):
                        continue
                    # 경계 요소가 없다면 실행
                    else:
                        visited[new_y_][new_x_] = 1
                        alpha_list.append(cakes[new_y_][new_x_])
                        q.append((new_x_, new_y_))
                        print("여기", alpha_list, new_x_, new_y_)
    return alpha_list

ca = ["KKKK", "KKKK", "KKKK", "FGHI"]
cr = [2, 3]
cc = [2]
print(solution(ca, cr, cc))