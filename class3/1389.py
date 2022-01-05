N, M = map(int,input().split())

INF = int(1e9)

graph = [[0] * (N+1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            # 시작점과 끝점이 같으면 안됨 
            if j != k and graph[j][i] and graph[i][k]:
                if graph[j][k] == 0:
                    graph[j][k] = graph[j][i] + graph[i][k]
                else:
                    graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

result = [sum([graph[i][j] for j in range(1, N+1)]) for i in range(1, N+1)]
print(result.index(min(result)) + 1)