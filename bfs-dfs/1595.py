import sys
from collections import defaultdict, deque

input = sys.stdin.readline

city = defaultdict(list)

while True:
    try:
        a, b, c = map(int, input().split())
        city[a].append((b, c))
        city[b].append((a, c))
    except:
        break

visited = [False] * 10001

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [False for __ in range(10001)]
    visited[start] = True
    max_dist = 0
    target_node = 0
    while q:
        cur_node, cur_dist = q.popleft()
        for next_node, next_dist in city[cur_node]:
            if visited[next_node]: 
                continue
            visited[next_node] = True
            dist = next_dist + cur_dist
            if dist > max_dist:
                max_dist, target_node = dist, next_node
            q.append((next_node, dist))
    return (target_node, max_dist)

start, answer = bfs(1)
_, answer = bfs(start)
print(answer)