n, m = map(int, input().split())
star = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    star[a].append(b)
    star[b].append(a)

distance = [0] * (n+1)
visited = [1]
def bfs(start, end):
    q = [start]

    while q:
        if len(visited) == n:
            break
        node = q.pop(0)

        for w in range(1, n+1):
            if w != node and w not in star[node] and w not in visited:
                visited.append(w)
                q.append(w)
                distance[w] = distance[node] + 1

                if w == end:
                    print(visited)
                    break
    
    return distance[end]

print(0)
for i in range(2, n+1):
    print(bfs(1, i))