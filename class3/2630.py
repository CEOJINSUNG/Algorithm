import sys

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

def solve(x, y, n):
    global white, blue
    num = paper[x][y]
    differ = False
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != paper[i][j]:
                differ = True
                break
    
    if differ:
        for i in range(2):
            for j in range(2):
                solve(x+n//2*i, y+n//2*j, n//2)
        return
    else:
        if paper[x][y] == 0:
            white += 1
        elif paper[x][y] == 1:
            blue += 1

solve(0, 0, N)
print(white)
print(blue)