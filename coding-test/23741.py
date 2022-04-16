import sys
input = sys.stdin.readline

n, m, x, y = map(int, input().split())

graph = [[] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

result = set()

q = [x]
number = [0] * (n+1)

while q:
    node = q.pop(0)
    
    if number[node] < y:
        for next in graph[node]:
            number[next] = number[node] + 1
            q.append(next)
    elif number[node] == y:
        result.add(node)

if result:
    print(*sorted(result))
else:
    print(-1)