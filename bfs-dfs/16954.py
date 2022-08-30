import sys
from collections import deque
input = sys.stdin.readline

miro = [list(input().rstrip()) for _ in range(8)]
move = [[0, 0], [0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [1, -1], [1, 1], [-1, 1]]
answer = 0

queue = deque()
queue.append((7, 0, 0))
    
while queue:
    x, y, turn = queue.popleft()
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
            
        if 0 <= nx < 8 and 0 <= ny < 8 and not miro[nx-turn][ny]=='#' and not miro[nx-turn-1][ny]=='#':
            if nx-turn < 0:
                answer = 1
                break
            queue.append([nx, ny, turn + 1])

print(answer)