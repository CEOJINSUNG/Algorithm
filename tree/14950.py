import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] !=x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m, t = map(int, input().split())

parent = [i for i in range(n+1)]
road = []
for _ in range(m):
    a, b, c = map(int, input().split())
    road.append((c, a, b))

road.sort()
line, answer = 0, 0
for c, a, b in road:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += c + line*t
        line += 1

print(answer)