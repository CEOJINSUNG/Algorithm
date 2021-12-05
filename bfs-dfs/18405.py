N, K = map(int, input().split())

virus = []
virus_position = dict()

for i in range(N):
    n_list = list(map(int, input().split()))
    virus.append(n_list)

    # 바이러스 위치 저장
    for j in range(N):
        if n_list[j] != 0:
            if n_list[j] in virus_position:
                virus_position[n_list[j]].append([j, i])
            else:
                virus_position[n_list[j]] = [[j, i]]

# 기존 x, y보다 1이 낮아야 함
s, x, y = map(int, input().split())

# 각 초마다 돌아야함
for _ in range(s):
    # 크기 오름차순으로 정렬
    sort_virus_position = sorted(virus_position.items(), key=lambda x: x[0])
    new_virus = dict()

    # 각 바이러스 마다 돌아야함
    for key, val in sort_virus_position:
        # 상하좌우
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for current_x, current_y in val:
            for m in range(4):
                new_x = current_x + dx[m]
                new_y = current_y + dy[m]
                if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N and virus[new_y][new_x] == 0:
                    virus[new_y][new_x] = key
                    if key in new_virus:
                        new_virus[key].append([new_x, new_y])
                    else:
                        new_virus[key] = [[new_x, new_y]]
    
    virus_position = new_virus

print(virus[x-1][y-1])
