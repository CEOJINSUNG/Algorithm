import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    parent = [0] * (n+1)
    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a
    
    v, w = map(int, input().split())
    
    v_path = [v]
    w_path = [w]

    while parent[v]:
        v_path.append(parent[v])
        v = parent[v]

    while parent[w]:
        w_path.append(parent[w])
        w = parent[w]
    
    v_level = len(v_path) - 1
    w_level = len(w_path) - 1

    while v_path[v_level] == w_path[w_level]:
        v_level -= 1
        w_level -= 1
    
    print(v_path[v_level+1])