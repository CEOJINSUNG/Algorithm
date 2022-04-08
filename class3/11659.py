import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = list(map(int, input().split()))

total = [0]
sum = 0

for i in range(len(array)):
    sum += array[i]
    total.append(sum)

for _ in range(m):
    x, y = map(int, input().split())
    print(total[y] - total[x-1])