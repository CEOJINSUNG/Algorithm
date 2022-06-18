import heapq
import sys
input = sys.stdin.readline

n = int(input())
left = []
right = []
answer = []
for _ in range(n):
    x = int(input())
    
    if len(left) == len(right):
        heapq.heappush(left, (-x, x))
    else:
        heapq.heappush(right, (x, x))
    
    if right and left[0][1] > right[0][0]:
        min_right = heapq.heappop(right)[0]
        max_left = heapq.heappop(left)[1]
        heapq.heappush(left, (-min_right, min_right))
        heapq.heappush(right, (max_left, max_left))
    
    answer.append(left[0][1])

for i in answer:
    print(i)