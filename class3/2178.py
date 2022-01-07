N, M = map(int, input().split())

miro = []

for _ in range(N):
    M_list = list(input())
    miro.append(M_list)

distance = [[0] * M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = [(0, 0)]
distance[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == M-1 and y == N-1:
        print(distance[y][x])
        break

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < M and 0 <= new_y < N:
            if miro[new_y][new_x] == '1' and distance[new_y][new_x] == 0:
                queue.append((new_x, new_y))
                distance[new_y][new_x] = distance[y][x] + 1

