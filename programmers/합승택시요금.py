def floyd(n, distances):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    distances[i][j] = 0
                elif distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances
    
def solution(n, s, a, b, fares):
    graph = [[int(1e9)]*(n) for _ in range(n)]
    for fare in fares:
        c, d, f = fare
        graph[c-1][d-1] = f
        graph[d-1][c-1] = f
    dist = floyd(n, graph)
    
    answer = int(1e9)
    for i in range(n):
        new_dist = dist[s-1][i] + dist[i][a-1] + dist[i][b-1]
        if answer > new_dist:
            answer = new_dist
    
    return answer