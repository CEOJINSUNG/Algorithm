n, q = map(int, input().split())

door_number = list(map(int, input().split()))

graph = {i: [] for i in range(n)}

if n == 1:
    print(door_number[0]%1000000007)
else:
    for i in range(n-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    def bfs(start, end):
        visited = []
        visited.append(start)
        queue = []
        queue.append([start])

        while queue:
            path = queue.pop(0)

            node = path[-1]

            if node == end:
                return path
            
            for adjacent in graph.get(node, []):
                if adjacent not in visited:
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.append(new_path)
                    visited.append(adjacent)

    for i in range(q):
        x, y = map(int, input().split())

        value = "".join(str(door_number[j]) for j in bfs(x-1, y-1))
        print(int(value)%1000000007)

# tree algorithm
# parent = [i for i in range(n+1)]

# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
    
#     return parent[x]


# def union(x, y):
#     x = find(x)
#     y = find(y)

#     if x < y:
#         parent[y] = x
#     else:
#         parent[x] = y

# for i in range(n-1):
#     a, b = map(int, input().split())
#     union(a, b)

# for i in range(q):
#     x, y = map(int, input().split())

# print(parent)