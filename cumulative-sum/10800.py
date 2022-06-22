import sys

n = int(input())
INF = 200000
balls = []

for i in range(n):
    color, size = map(int, sys.stdin.readline().split())
    balls.append((size, color, i))

balls.sort()
color_count = [0] * (INF + 1)
total = 0
j = 0
ans = [0] * (n + 1)
for i in range(n):
    while balls[j][0] < balls[i][0]:
        color_count[balls[j][1]] += balls[j][0]
        total += balls[j][0]
        j += 1
    ans[balls[i][2]] = total - color_count[balls[i][1]]

for i in range(n):
    print(ans[i])