from collections import defaultdict
import sys, heapq

n = int(sys.stdin.readline())

degree = defaultdict(int)
graph = defaultdict(list)
for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    if degree[a]:
        pass
    else:
        degree[a] = 0
    
    degree[b] += 1
    graph[a].append(b)

def topology():
    result = []
    q = []
    temp = []

    for key, value in degree.items():
        if value == 0:
            heapq.heappush(q, key)
    
    while q:
        current_item = heapq.heappop(q)
        
        result.append(current_item)
    
        for item in graph[current_item]:
            degree[item] -= 1

            if degree[item] == 0:
                heapq.heappush(temp, item)
        
        if len(q) == 0:
            q = temp
            temp = []

    return result


result = topology()

if len(degree.keys()) == len(set(result)):
    for k in result:
        print(k)
else:
    print(-1)