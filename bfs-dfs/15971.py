from collections import deque

n, robot_1, robot_2 = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

INF = int(1e9)

def bfs(start, end):
    visited = [False] * (n + 1)

    q = deque()
    q.append((start, 0, 0))
    visited[start] = 0

    while q:
        cur_node, cur_total, cur_max_cost = q.popleft()
        
        if cur_node == end:
            return cur_total - cur_max_cost
        
        for next_node, next_cost in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.appendleft((next_node, cur_total + next_cost, max(cur_max_cost, next_cost)))

print(bfs(robot_1, robot_2))
