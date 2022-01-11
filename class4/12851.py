from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

road = [-1] * 100001
count = [0] * 100001
queue = deque()
queue.append(N)
road[N] = 0
count[N] = 1

while queue:
    node = queue.popleft()

    for i in (node - 1, node + 1, node * 2):
        if 0 <= i <= 100000:
            if road[i] == -1:
                road[i] = road[node] + 1
                count[i] = count[node]
                queue.append(i)
            elif road[i] == road[node] + 1:
                count[i] += count[node]

print(road[K])
print(count[K])