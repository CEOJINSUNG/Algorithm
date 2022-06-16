from collections import deque

f, s, g, u, d = map(int, input().split())

exist = -1
visited = [0] * (f+1)
q = deque()
q.append((0, s))
visited[s] = 0

while q:
    count, floor = q.popleft()

    if floor == g:
        exist = count
        break
    
    down = floor - d
    up = floor + u
    if floor > d and visited[down] == 0:
        visited[down] = count + 1
        q.append((count+1, down))
    if floor + u <= f and visited[up] == 0:
        visited[up] = count + 1
        q.append((count+1, up))

if exist == -1:
    print("use the stairs")
else:
    print(exist)