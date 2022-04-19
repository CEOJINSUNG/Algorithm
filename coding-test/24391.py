n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

code = list(map(int, input().split()))
count = 0

for i in range(n-1):
    a = find(code[i])
    b = find(code[i+1])

    if a != b:
        count += 1

print(count)