# 동굴의 높이와 넓이 입력 받가
R, C = map(int, input().split())

# 동굴의 크기 선언 및 미네랄 입력받기
cave = [[] for _ in range(R)]
for i in range(R):
    C_list = input()
    cave[i].extend(list(C_list))

# 막대를 던진 횟수
N = int(input())

# 막대를 던진 위치
throw_stick = list(map(int, input().split()))

# 미네랄 위치를 찾아 변환하는 함수
def find_mineral(height, direction):
    mineral_position = [index for index, value in enumerate(cave[height]) if value == "x"]

    # 미네랄이 있다면
    if len(mineral_position) != 0:
        # 방향이 왼쪽이라면
        if direction%2 == 0:
            cave[height][mineral_position[0]] = "."
            del mineral_position[0]
            return find_below(mineral_position, height)
        # 방향이 오른쪽이라면
        else:
            cave[height][mineral_position[-1]] = "."
            del mineral_position[-1]
            return find_below(mineral_position, height)
    
    # 미네랄이 없다면
    return find_below(mineral_position, height)

# 가장 아래쪽에 있는 미네랄을 찾기
def find_below(mineral_position, height_over):
    # 미네랄이 없다면
    if not mineral_position:
        if height_over != 0:
            # 더 높은 곳부터살펴봄
            for i in reversed(range(height_over)):
                below_mineral = [index for index, value in enumerate(cave[i]) if value == "x"]

                # 만약 x가 위에서 발견했다면 그거를 가지고 옴
                if below_mineral:
                    minmum_below = []
                    # 발견한 x마다 아래로 갔을 때 발견한 바닥 및 미네랄과의 높이를 구함
                    for j in below_mineral:
                        for k in range(i+1, R):
                            # 바닥
                            if k == R-1:
                                minmum_below.append([j, R-1-i])
                                break
                            # 미네랄
                            elif cave[k][j] == "x":
                                minmum_below.append([j, k-i-1])
                                break
                    # 발견한 x의 [column 위치, [row위치, 아래로 가야하는 길이]]
                    return [i, minmum_below]
            return []
        else:
            return []
    # 막대로 제거 이후에 같은 줄에 미네랄이 있다면
    else:
        minmum_below = []
        for j in mineral_position:
            # 발견한 x마다 아래로 갔을 때 발견한 바닥 및 미네랄과의 높이를 구함
            for k in range(height+1, R):
                # 바닥
                if k == R-1 and cave[k][j] == '.':
                    minmum_below.append([j, R-1-height])
                    break
                # 미네랄
                elif cave[k][j] == "x":
                    minmum_below.append([j, k-height])
                    break
        # 발견한 x의 [column 위치, [row위치, 아래로 가야하는 길이]]를 받음
        return [height_over, minmum_below]

# bfs 선언
def bfs(x, y):
    # 상하좌우에 필요한 좌표
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    # 방문한 위치
    visited = []

    # 큐 선언
    q = []

    # 초기 좌표 삽입
    visited = [[x, y]]

    # column == R-1인 경우 찾기
    connected = False
    q.append((x, y))

    while q:
        x_, y_ = q.pop(0)

        for i in range(4):
            new_x_ = x_ + dx[i]
            new_y_ = y_ + dy[i]
            if 0 <= new_x_ < C and 0 <= new_y_ < R and cave[new_y_][new_x_] == "x" and [new_x_, new_y_] not in visited:
                visited.append([new_x_, new_y_])
                q.append((new_x_, new_y_))
                if new_y_ == R - 1:
                    connected = True
    if connected:
        return []
    else:
        return visited


for i in range(N):
    height = R-throw_stick[i]
    mineral = find_mineral(height, i)

    # 발견한 x의 위치마다 BFS를 수행해서 column == R-1인 경우가 있다면 아래로 연결되어 있다는 의미이고 
    # 없다면 고립되어 있는 것이므로 가장 낮은 거리를 가진 요소를 기준으로 아래로 내림
    if mineral:
        y = mineral[0]
        for j in mineral[1]:
            visit_result = bfs(j[0], y)
            # 만약 고립되어 있다면
            if visit_result:
                for position in visit_result:
                    x = position[0]
                    old_y = position[1]
                    new_y = position[1] + j[1]
                    cave[old_y][x] = "."
                    cave[new_y][x] = "x"
                

for a in cave:
    print(''.join(a))
