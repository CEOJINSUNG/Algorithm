import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    tmp = int(input())
    if tmp == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, tmp)