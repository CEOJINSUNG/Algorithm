from heapq import heappush, heappop
from collections import deque, defaultdict

INF = int(1e9)

def dijkstra(n, graph, start):
    distance = [INF] * (n + 1)
    path = []
    heappush(path, (0, start))
    distance[start] = 0
    
    while path:
        cost, node = heappop(path)
        
        if distance[node] < cost:
            continue
            
        for next_node in graph[node]:
            if cost + 1 < distance[next_node]:
                distance[next_node] = cost + 1
                heappush(path, (cost + 1, next_node))
    return distance

def solution(n, roads, sources, destination):
    answer = []
    graph = defaultdict(list)
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = dijkstra(n, graph, destination)
    
    for start in sources:
        if distance[start] == INF:
            answer.append(-1)
        else:
            answer.append(distance[start])
    return answer