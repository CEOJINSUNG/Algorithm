# 특정 원소가 속한 집합 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
    
# 두 원소가 속한 집합 찾기
def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

# 노드의 개수와 간선의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n+1)

edges = []
result = 0
MST = []

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
        MST.append((a, b))
        if len(MST) == n-2:
            break
print(result)