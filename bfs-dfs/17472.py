import sys

# n, m input
n, m = map(int, sys.stdin.readline().split())

# sea, land
land = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    land.append(list(map(int, sys.stdin.readline().split())))

# position of island
island = []

# Using BFS, find an individual algorithm
def bfs(x, y):
    q = [(x, y)]
    coordinate = set()
    coordinate.add((x, y))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        current_x, current_y = q.pop(0)

        for i in range(4):
            new_x = current_x + dx[i]
            new_y = current_y + dy[i]

            if 0 <= new_x < m and 0 <= new_y < n and land[new_y][new_x] == 1 and visited[new_y][new_x] == False:
                visited[new_y][new_x] = True
                coordinate.add((new_x, new_y))
                q.append((new_x, new_y))
    return coordinate

for i in range(n):
    for j in range(m):
        if land[i][j] == 1 and visited[i][j] == False:    
            island.append(bfs(j, i))


# Using Brute force, find the distance of two islands
edges = []

for i in range(len(island)):
    for j in range(len(island)):
        if i != j:
            min_distance = 101
            
            for x, y in island[i]:
                for next_x, next_y in island[j]:
                    if x == next_x:
                        if abs(y - next_y) > 2:
                            flag = False
                            bigger = max(y, next_y)
                            smaller = min(y, next_y)

                            for k in range(smaller+1, bigger):
                                if land[k][x] == 1:
                                    flag = True
                                    break
                            
                            if flag == False:
                                min_distance = min(min_distance, abs(y - next_y)-1)
                    
                    if y == next_y:
                        if abs(x - next_x) > 2:
                            flag = False
                            bigger = max(x, next_x)
                            smaller = min(x, next_x)

                            for k in range(smaller+1, bigger):
                                if land[y][k] == 1:
                                    flag = True
                                    break
                            
                            if flag == False:
                                min_distance = min(min_distance, abs(x - next_x)-1)
            
            if min_distance != 101 and (min_distance, j, i) not in edges:
                edges.append((min_distance, i, j)) 

edges.sort()
# Using mst Algorithm, find the minimum spanning tree
parent = [i for i in range(len(island))]

answer = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x <= y:
        parent[y] = x
    else:
        parent[x] = y

edges.sort()
final = set()

for edge in edges:
    weight, x, y = edge
    if find(x) != find(y):
        final.add(x)
        final.add(y)
        union(x, y)
        answer += weight

wrong = False
for i in range(len(island)):
    for j in range(len(island)):
        if find(i) != find(j):
            wrong = True
            break
    if wrong:
        break

if edges and wrong == False:
    print(answer)
else:
    print(-1)