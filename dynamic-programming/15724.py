import sys

n, m = map(int, sys.stdin.readline().split())
earth = []

for _ in range(n):
    people = list(map(int, sys.stdin.readline().split()))

    division = []
    total = 0
    for i in people:
        total += i
        division.append(total)
    
    earth.append(division)

def divisionCalculate(x, y):
    if x < 0 or y < 0:
        return 0
    else:
        width = 0
        for i in range(y+1):
            width += earth[i][x]
        return width

def calculate(x1, y1, x2, y2):
    entire = 0
    
    # (0, 0) ~ (x2, y2)
    entire += divisionCalculate(x2, y2)

    # (0, 0) ~ (x1-1, y1-1)
    entire += divisionCalculate(x1-1, y1-1)

    # (0, 0) ~ (x2, y1-1)
    entire -= divisionCalculate(x2, y1-1)

    # (0, 0) ~ (x1-1, y2)
    entire -= divisionCalculate(x1-1, y2)

    return entire

k = int(sys.stdin.readline())
for _ in range(k):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    print(calculate(x1-1, y1-1, x2-1, y2-1))