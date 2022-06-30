import heapq

def solution(N, road, K):
    answer = 0
    
    dist = [int(1e9)]*(N+1)
    village = [[] for _ in range(N+1)]
    for a, b, c in road:
        village[a].append((c, b))
        village[b].append((c, a))
    
    dist[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    
    while q:
        d, node = heapq.heappop(q)
        
        if dist[node] < d:
            continue
        
        for w, a in village[node]:
            if dist[a] > d + w:
                dist[a] = d + w
                heapq.heappush(q, (d+w, a))
    
    for i in range(1, N+1):
        if dist[i] <= K:
            answer += 1
    
    return answer