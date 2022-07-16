import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
wheel = [deque(map(int, input().strip())) for _ in range(t)]

def move(n, d):
    global cur_right, cur_left, wheel
    origin_dir = d

    for i in reversed(range(n)):
        if wheel[i][2] != cur_left:
            cur_left = wheel[i][6]
            wheel[i].rotate(d*-1)
            d*=-1
        else:
            break
    
    d = origin_dir
    for i in range(n+1, t):
        if wheel[i][6] != cur_right:
            cur_right = wheel[i][2]
            wheel[i].rotate(d*-1)
            d*=-1
        else:
            break

k = int(input())
for _ in range(k):
    n, d = map(int, input().split())
    cur_left, cur_right = wheel[n-1][6], wheel[n-1][2]
    wheel[n-1].rotate(d)
    move(n-1, d)

print(sum([1 if wheel[0] else 0 for delta, wheel in enumerate(wheel)]))