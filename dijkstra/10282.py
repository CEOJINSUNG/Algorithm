import heapq

INF = float('inf')
test = int(input())

def dijkstra(number, graph, start):
    distances = {i+1: INF for i in range(number)}

    distances[start] = 0
    queue = []

    heapq.heappush(queue, (distances[start], start))

    while queue:
        second, node = heapq.heappop(queue)

        if distances[node] < second:
            continue

        for next_node, next_second in graph[node].items():
            weighted = second + next_second

            if weighted < distances[next_node]:
                distances[next_node] = weighted
                heapq.heappush(queue, (weighted, next_node))
    
    return distances

for _ in range(test):
    n, d, c = map(int, input().split())
    computer = {i+1: {} for i in range(n)}

    for _ in range(d):
        a, b, s = map(int, input().split())
        computer[b][a] = s
    
    result = dijkstra(n, computer, c)
    number = 0
    max_time = 0
    for value in result.values():
        if value != INF:
            number += 1
            max_time = max(max_time, value)

    print(number, max_time)