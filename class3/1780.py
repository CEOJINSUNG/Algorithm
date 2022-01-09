N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

count = {
    -1: 0,
    0: 0,
    1: 0
}

def matrix_cut(x, y, num):
    differ = False
    num_check = matrix[x][y]
    for i in range(x, x+num):
        for j in range(y, y+num):
            if matrix[i][j] != num_check:
                differ = True
                break
    
    if differ:
        for i in range(3):
            for j in range(3):
                matrix_cut(x+i*num//3, y+j*num//3, num//3)
    else:
        count[num_check] += 1

matrix_cut(0, 0, N)

for v in count.values():
    print(v)