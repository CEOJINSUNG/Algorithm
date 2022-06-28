import sys
input = sys.stdin.readline
INF = int(1e9) + 1


array = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    array.append((x, y))

answer, l, r = 0, -INF, -INF
array.sort()
for i in range(n):
    if array[i][0] < r:
        r = max(r, array[i][1])
    else:
        answer += (r-l)
        l = array[i][0]
        r = array[i][1]

answer += r - l
print(answer)