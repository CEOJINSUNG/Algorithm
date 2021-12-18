n = int(input())

cal_x, cal_y = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(graph, start, end):
    q = []
    visited = []
    count = 0
    q.append(start)

    while q:
        count += 1

        for _ in range(len(q)): 
            position = q.pop(0)
            if position == end:
                return count - 1
            for node in graph[position]:
                if node not in visited:
                    visited.append(node)
                    q.append(node) 

    return -1

print(bfs(graph, cal_x, cal_y))