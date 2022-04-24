import sys, heapq

n, c = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

village = [c for _ in range(n)]
box = []
for _ in range(m):
    start, end, amount = map(int, sys.stdin.readline().split())
    box.append([(amount / (end-start)), start, end, amount])

box.sort(key=lambda x: (x[2], -x[1]))

print(box)

answer = 0
while box:
    rate, start, end, amount = box.pop(0)

    min_value = min(village[start:end])

    if min_value == 0:
        pass

    shipping_amount = min(min_value, amount)
    answer += shipping_amount

    for i in range(start, end):
        village[i] -= shipping_amount

print(answer)