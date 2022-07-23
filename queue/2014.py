import heapq
K, N = map(int, input().split())
prime = list(map(int, input().split()))

pq = []
for num in prime:
    heapq.heappush(pq, num)

for i in range(N):
    num = heapq.heappop(pq)
    for j in range(K):
        new_num = num * prime[j]
        heapq.heappush(pq, new_num)

        if num % prime[j] == 0:
            break
else:
    print(num)