import sys
input = sys.stdin.readline

n = int(input())

result = 0
left = 30
for _ in range(n):
    t = int(input())

    if t < left:
        result += 1
        left -= t
    elif t == left:
        result += 1
        left = 30
    else:
        half = left/float(t)
        if half >= 0.5:
            result += 1
        left = 30

print(result)