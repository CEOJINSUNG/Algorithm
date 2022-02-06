import heapq

N, M = map(int, input().split())

heap = []

for _ in range(M):
    a, b = map(int, input().split())
    heapq.heappush(heap, (a, [a, b]))

answer = []
while heap:
    answer.extend(heapq.heappop(heap)[1])

not_include = [i for i in range(1, N+1) if i not in answer]
answer.extend(not_include)
print(*answer)