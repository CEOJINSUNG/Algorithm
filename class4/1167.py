import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]

for _ in range(V):
    data = list(map(int, input().split()))
    for i in range(1, len(data)-1, 2):
        tree[data[0]].append((data[i], data[i+1]))

def bfs(start):
    queue = [start]
    visited = [-1] * (V+1)
    visited[start] = 0

    max = [0, 0]

    while queue:
        node = queue.pop()
        for i in tree[node]:
            if visited[i[0]] == -1:
                visited[i[0]] = visited[node] + i[1]
                queue.append(i[0])

                if max[0] < visited[i[0]]:
                    max[0] = visited[i[0]]
                    max[1] = i[0]
    
    return max

temp, one = bfs(1)
answer, two = bfs(one)
print(answer)