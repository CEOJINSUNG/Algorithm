V, E = map(int, input().split())

parent = {i : i for i in range(1, V+1)}
rank = {i : 0 for i in range(1, V+1)}
graph_edges = []

for _ in range(E):
    A, B, C = map(int, input().split())
    graph_edges.append([C, A, B])

# 해당 vertice의 최상위 정점을 찾기
def find(vertices):
    if parent[vertices] != vertices:
        parent[vertices] = find(parent[vertices])
    return parent[vertices]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(edges):
    mst = []
    edges.sort()

    for edge in edges:
        w, v1, v2 = edge
        if find(v1) != find(v2):
            union(v1, v2)
            mst.append(w)

    return sum(mst)

print(kruskal(graph_edges))