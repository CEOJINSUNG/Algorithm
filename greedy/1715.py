import sys
import heapq

input = sys.stdin.readline

N = int(input())
card = []
for _ in range(N):
    heapq.heappush(card, int(input()))

if N == 1:
    print(0)
else:
    result = []

    while card:
        first = heapq.heappop(card)
        second = heapq.heappop(card)

        result.append(first + second)

        if len(card) == 0:
            break
        else:
            heapq.heappush(card, first + second)
    
    print(sum(result))