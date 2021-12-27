import heapq

def dijkstra(start, distance):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (distance[start], start))
    
    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] < dist:
            continue

        for next in graph[node]:
            weighted_distance = dist + next[1]
            if weighted_distance < distance[next[0]]:
                distance[next[0]] = weighted_distance
                heapq.heappush(queue, (weighted_distance, next[0]))