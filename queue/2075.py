import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    row = list(map(int, input().split()))
    if not heap:
        for i in row:
            heapq.heappush(heap, i)
    else:
        for i in row:
            if heap[0] < i:
                heapq.heappush(heap, i)
                heapq.heappop(heap)

print(heap[0])