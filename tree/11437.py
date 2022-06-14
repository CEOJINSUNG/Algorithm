import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

level = [0] * (n+1)
parent = [0] * (n+1)
def set_tree(node, pnode):
    parent[node] = pnode
    level[node] = level[pnode] + 1

    for i in range(len(tree[node])):
        child = tree[node][i]
        if child == pnode: continue
        set_tree(child, node)

def lca(a, b):
    if level[a] < level[b]:
        a, b = b, a
    
    while level[a] != level[b]:
        a = parent[a]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a

set_tree(1, 0)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))