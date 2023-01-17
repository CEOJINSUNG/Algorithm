from collections import deque

test = int(input())

for _ in range(test):
    h, w = map(int, input().split())

    grid = [list(input()) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]

    answer = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and grid[i][j] == "#":
                q = deque()
                q.append((j, i))
                visited[i][j] = 1
                
                while q:
                    col, row = q.popleft()

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_col, new_row = col + dx, row + dy

                        if 0 <= new_col < w and 0 <= new_row < h and visited[new_row][new_col] == 0:
                            if grid[new_row][new_col] == "#":
                                q.append((new_col, new_row))
                                visited[new_row][new_col] = 1
                
                answer += 1
    
    print(answer)