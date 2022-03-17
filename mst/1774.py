import sys
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 크루스칼 알고리즘
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x]) # 부모 테이블 갱신
    return parent[x]

def union(x, y): 
    x = find(x) 
    y = find(y)

    if x == y: # 동일한 집합일 경우
        return

    if x < y:
        parent[y] = x 
    else: 
        parent[x] = y

def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(1/2)

N,M = map(int,input().split())
point = [] 
parent = [i for i in range(N+1)]
edges = []
result = 0

for _ in range(N):
    x, y = map(int, input().split())
    point.append((x, y))

for _ in range(M):
    x, y = map(int, input().split())
    union(x-1, y-1)

# 모든 point 간에 간선, 비용 계산 저장
for i in range(N - 1):
    for j in range(i+1, N):
        edges.append((dist(point[i], point[j]), i, j))

edges.sort(key = lambda x : x[0])

for e in edges:
    cost, x, y = e
    if find(x) != find(y):
        union(x, y)
        result += cost

print('%.2f' %(result))