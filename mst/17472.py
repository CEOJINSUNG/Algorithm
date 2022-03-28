from collections import defaultdict

# n, m input
n, m = map(int, input().split())

# sea, land
land = []

for _ in range(n):
    one = list(map(int, input().split()))
    land.append(one)

# for bfs algorithm
visited = [[False] * m for _ in range(n)]

# position of island
island = defaultdict(list)
island_number = 0

# Using BFS, find an individual algorithm
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and land[i][j] == 1:
            visited[i][j] = True
            q = []
            q.append((i, j))

            chunk = []
            chunk.append((i, j))

            while q:
                x_, y_ = q.pop(0)

                for k in range(4):
                    new_x = x_ + dx[k]
                    new_y = y_ + dy[k]

                    if 0 <= new_x < n and 0 <= new_y < m and visited[new_x][new_y] == False and land[new_x][new_y] == 1:
                        visited[new_x][new_y] = True
                        q.append((new_x, new_y))
                        chunk.append((new_x, new_y))
                
            island[island_number] = chunk
            island_number += 1

# Using Brute force, find the distance of two islands
edges = []

for i in range(island_number):
    if island_number == 1:
        break
    for j in range(i+1, island_number):
        min_distance = 101
        for x, y in island[i]:
            for new_x, new_y in island[j]:
                if new_x == x:
                    distance = abs(y-new_y) - 1
                    if distance <= 1:
                        min_distance = 101
                        break
                    elif distance <= min_distance and distance > 1:
                        min_distance = distance
                    
                elif new_y == y:
                    distance = abs(x-new_x) - 1
                    if distance <= 1:
                        min_distance = 101
                        break
                    elif distance <= min_distance and distance > 1:
                        min_distance = distance

        edges.append((min_distance, i, j))        

# Using mst Algorithm, find the minimum spanning tree
parent = [i for i in range(island_number)]

answer = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

edges.sort()

for edge in edges:
    weight, x, y = edge
    if find(x) != find(y):
        union(x, y)
        answer += weight

if answer >= 100:
    print(-1)
else:
    print(answer)