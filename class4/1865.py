from dis import dis
import sys
input = sys.stdin.readline
INF = sys.maxsize

def bellmanFord():
    dist = {i: INF for i in range(1, N+1)}

    for i in range(1, N+1):
        for j in range(1, N+1):
            for w, d in edges[j]:
                if dist[d] > w + dist[j]:
                    dist[d] = w + dist[j]
                    if i == N:
                        return "YES"
    return "NO"

TC = int(input())
for _ in range(TC):
    N, M, W =  map(int, input().split())
    edges = [[] for _ in range(N+1)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        edges[S].append((T, E))
        edges[E].append((T, S))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges[S].append((-T, E))

    print(bellmanFord())