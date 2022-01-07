computer = int(input())
pair = int(input())

graph = [[] for _ in range(computer+1)]

for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []
queue = [1]

while queue:
    node = queue.pop(0)

    if node not in visited:
        visited.append(node)
        queue.extend(graph[node])

print(len(visited) - 1)