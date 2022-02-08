import heapq

N, K = map(int, input().split())

jewelry = []
for _ in range(N):
    M, V = map(int, input().split())
    heapq.heappush(jewelry, [M, V])

bag = []
for _ in range(K):
    C = int(input())
    heapq.heappush(bag, C)

answer = 0
enable_jewelry = []

for _ in range(K):
    c = heapq.heappop(bag)

    while jewelry and c >= jewelry[0][0]:
        [w, v] = heapq.heappop(jewelry)
        heapq.heappush(enable_jewelry, -v)
    
    if enable_jewelry:
        answer -= heapq.heappop(enable_jewelry)
    elif not jewelry:
        break

print(answer)