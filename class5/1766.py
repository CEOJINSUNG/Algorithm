import heapq

n, m = map(int, input().split())

indegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology():
    global indegree
    result = []
    q = []

    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
    
    while q:
        current = heapq.heappop(q)
        result.append(current)

        for i in graph[current]:
            indegree[i] -= 1

            if indegree[i] == 0:
                heapq.heappush(q, i)
    
    for i in result:
        print(i, end=' ')

topology()