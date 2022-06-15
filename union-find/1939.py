import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
maps = [[] for _ in range(n+1)]

for _ in range(m):
    y, x, w = map(int, sys.stdin.readline().split())
    maps[y].append((x,w))
    maps[x].append((y,w))

start, end = map(int, sys.stdin.readline().split())

_min, _max = 1, 1000000000

def bfs(c):
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    result = []
    while queue:
        y = queue.popleft()
        for x, w in maps[y]:
            if x not in visited and w >= c:
                visited.add(x)
                queue.append(x)
    
    return True if end in visited else False

result = _min
while _min <= _max:
    mid = (_min + _max) // 2
    if bfs(mid):
        result = mid
        _min = mid + 1
    else:
        _max = mid - 1
print(result)
        
    