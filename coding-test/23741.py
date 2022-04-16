n, m, x, y = map(int, input().split())

graph = [[] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

check = [[0] * 1001 for _ in range(1001)]

def bfs(x, y):
    q = [(x, 1)]
    check[x][1] = 1
    result = set()
    
    while q:
        node, depth = q.pop(0)

        if depth > y:
            break

        next = graph[node]

        for i in next:
            if check[i][depth+1] == 1: continue
            check[i][depth+1] = 1
            q.append((i, depth+1))

            if depth == y:
                result.add(i)
    
    result = sorted(list(result))

    if len(result) == 0:
        print(-1)
        return
    
    print(*result)

bfs(x, y)