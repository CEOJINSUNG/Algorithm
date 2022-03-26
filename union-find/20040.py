from re import L
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 부모노드 생성
parent = [i for i in range(n+1)]

def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a == b:
        return True
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    return False

answer = 0

for i in range(m):
    a, b = map(int, input().split())
    # 최초 사이클 생성이기 때문에 answer가 갱신되기 전에 해야하고 
    # 또한, union을 했을 때에도 True가 나오는 지점을 알 수 있다.
    if union(parent, a, b) and answer == 0:
        answer = i + 1

print(answer)