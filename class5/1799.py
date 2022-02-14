N = int(input())

chess = []
black, white = [], []
color = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        color[i][j] = (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0)

for i in range(N):
    chess.append(list(map(int, input().split())))
    for j in range(N):
        if chess[i][j] == 1 and color[i][j] == 1:
            black.append((i, j))
        if chess[i][j] == 1 and color[i][j] == 0:
            white.append((i, j))

black_count, white_count = 0, 0
isused01 = [0] * (N*2-1)
isused02 = [0] * (N*2-1)

def find(bishop, index, count):
    global black_count, white_count
    if index == len(bishop):
        rx, ry = bishop[index-1]
        if color[rx][ry]:
            black_count = max(black_count, count)
        else:
            white_count = max(white_count, count)
        return
    
    x, y = bishop[index]
    if isused01[x+y] or isused02[x-y+N-1]:
        find(bishop, index+1, count)
    else:
        isused01[x+y] = 1
        isused02[x-y+N-1] = 1
        find(bishop, index+1, count+1)
        isused01[x+y] = 0
        isused02[x-y+N-1] = 0
        find(bishop, index+1, count)

if len(black) > 0:
    find(black, 0, 0)
if len(white) > 0:
    find(white, 0, 0)

print(black_count+white_count)