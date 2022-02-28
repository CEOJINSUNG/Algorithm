def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
c = []

for i in range(N):
    x, y, z = map(int, input().split())
    c.append((x, y, z, i))

edges = []
for i in range(3):
    c.sort(key=lambda x:x[i])
    for j in range(1, N):
        edges.append((abs(c[j-1][i]-c[j][i]), c[j-1][3], c[j][3]))

parent = [i for i in range(N)]
total = 0
edges.sort()

for i in range(len(edges)):
    if find(edges[i][1], parent) != find(edges[i][2], parent):
        union(edges[i][1], edges[i][2], parent)
        total += edges[i][0]

print(total)