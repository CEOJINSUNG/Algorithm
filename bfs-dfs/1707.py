from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, color, status):
    q = deque()
    q.append(start)

    color[start] = status

    while q:
        node = q.popleft()

        for next in graph[node]:
            if color[next] == 0:
                q.append(next)
                color[next] = color[node] * -1
            elif color[node] + color[next] != 0:
                return False
    return True

test = int(input())
for _ in range(test):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    color = [0]*(v+1)
    check = True

    for i in range(1, v+1):
        if check == False:
            break
        if color[i] == 0:
            check = bfs(graph, i, color, 1)
    
    if check:
        print("YES")
    else:
        print("NO")