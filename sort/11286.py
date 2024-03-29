import sys, heapq

n = int(sys.stdin.readline())
h = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(x), x))