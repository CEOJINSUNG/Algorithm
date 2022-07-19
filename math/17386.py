x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def ccw(x1, y1, x2, y2, x3, y3):
    answer = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if answer < 0:
        return -1
    elif answer > 0:
        return 1
    else:
        return 0

A = ccw(x1, y1, x2, y2, x3, y3)
B = ccw(x1, y1, x2, y2, x4, y4)
C = ccw(x3, y3, x4, y4, x1, y1)
D = ccw(x3, y3, x4, y4, x2, y2)

if A*B < 0 and C*D < 0:
    print(1)
else: 
    print(0)
