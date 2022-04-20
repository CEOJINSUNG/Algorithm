import sys

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())

def find(x):
    if gate[x] != x:
        gate[x] = find(gate[x])
    
    return gate[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        gate[b] = a
    else:
        gate[a] = b

gate = [i for i in range((g+1))]

answer = 0
for i in range(1, p+1):
    docking = int(sys.stdin.readline())
    parent = find(docking)

    if parent == 0:
        break
    else:
        answer += 1
        union(parent, parent-1)

print(answer)