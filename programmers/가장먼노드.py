import heapq

def dijkstra(start, graph, n):
    heap = []
    heapq.heappush(heap, (0, start))
    
    visited = [int(1e9) for i in range(n+1)]
    visited[start] = 0
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        if visited[node] < dist:
            continue
        
        for next in graph[node]:
            new_dist = dist + 1
            if visited[next] > new_dist:
                visited[next] = new_dist
                heapq.heappush(heap, (new_dist, next))
    
    return visited

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    dist = dijkstra(1, graph, n)[1:]
    far = max(dist)
    answer = dist.count(far)
    return answer