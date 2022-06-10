from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
zoo = []
for _ in range(h):
    zoo.append(list(map(int, input().split())))

horse_dx = [1, 1, 2, 2, -1, -1, -2, -2]
horse_dy = [2, -2, 1, -1, 2, -2, 1, -1]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0, k))

    visit = [[[0 for _ in range(31)] for _ in range(w)] for _ in range(h)]  
    while q:
        x, y, count = q.popleft()

        if x == w-1 and y == h-1:
            return visit[y][x][count]
        
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
                
            if 0 <= new_x < w and 0 <= new_y < h:
                if zoo[new_y][new_x] == 0 and visit[new_y][new_x][count] == 0:
                    q.append((new_x, new_y, count))
                    visit[new_y][new_x][count] = visit[y][x][count] + 1

        if count > 0:
            for i in range(8):
                new_x, new_y = x + horse_dx[i], y + horse_dy[i]

                if 0 <= new_x < w and 0 <= new_y < h:
                    if zoo[new_y][new_x] == 0 and visit[new_y][new_x][count-1] == 0:
                        visit[new_y][new_x][count-1] = visit[y][x][count] + 1
                        q.append((new_x, new_y, count - 1))
        
    return -1
    
print(bfs())