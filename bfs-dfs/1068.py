from collections import deque
import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n)]

root = 0
parent = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    if parent[i] == -1:
        root = i
    else:
        tree[parent[i]].append(i)

delete = int(sys.stdin.readline())

def dfs(start):
    visited = []

    q = deque()
    q.append(start)

    leaf = 0

    while q:
        current_node = q.pop()

        if current_node in set(visited):
            continue

        visited.append(current_node)
        
        if len(tree[current_node]) == 0 or len(set(tree[current_node])-set([delete])) == 0:
            leaf += 1
        
        for next_node in tree[current_node]:
            if next_node == delete:
                continue
            q.append(next_node)
    return leaf

if root == delete: print(0)
else: print(dfs(root))