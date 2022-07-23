import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))

heapq.heapify(card)
for _ in range(m):
    one = heapq.heappop(card)
    two = heapq.heappop(card)

    merge = one + two
    heapq.heappush(card, merge)
    heapq.heappush(card, merge)

print(sum(card))