N = -1
case = 0

while True:
    # N을 입력 받음
    N = int(input())

    # N이 0이면 멈춤
    if N == 0:
        break
    
    case += 1
    # N이 0이 아닌 경우
    # 초기 동굴 배열 선언
    cave = [[0 for i in range(N)] for j in range(N)]

    # 동굴 배열의 가중치 값 집어넣기
    for i in range(N):
        cave_inner = list(map(int, input().split()))
        cave[i] = cave_inner
    
    # 내가 원하는 위치로 가기 위해서 최소 가중치를 더한 값이 저장된 배열 선언
    minimum_weight = [[0 for i in range(N)] for j in range(N)]

    # 3번 조건 초기 값 선언
    minimum_weight[0][0] = cave[0][0]

    # 각 위치에 가기 위한 최솟값 구하기
    for i in range(N):
        for j in range(N):
            # minimum_weight[0][j]는 왼쪽에서 오른쪽으로 가는게 최솟값임
            if i == 0 and j > 0: 
                minimum_weight[i][j] = minimum_weight[i][j-1] + cave[i][j]
            # minimum_weight[i][0]은 위에서 아래쪽으로 가는게 최솟값임
            elif j == 0 and i > 0:
                minimum_weight[i][j] = minimum_weight[i-1][j] + cave[i][j]
            # 그 외의 값은 2번 조건을 적용해 min 값을 구함
            else:
                minimum_weight[i][j] = min(
                    # 위에서 아래니까 i-1, j임
                    minimum_weight[i-1][j],
                    # 왼쪽에서 오른쪽이니까 i, j-1임
                    minimum_weight[i][j-1]
                ) + cave[i][j]

    # 최종적으로 1번 조건을 성립해야 하기에 [N-1][N-1] 값을 출력
    print("Problem {0}: {1}".format(case, minimum_weight[N-1][N-1]))


