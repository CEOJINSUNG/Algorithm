# 목적 : 탐험할 수 있는 구역의 개수를 출력한다. 
# 첫 번째 줄에 N과 M이 공백을 사이에 두고 주어진다.
# 두 번째 줄부터 N개의 줄에 걸쳐 N x M개의 칸에 대한 정보가 주어진다. 
# 두 번째 줄에서부터 i번째 줄에 주어지는 j번째 정수는 칸 (i-1, j-1)에 대한 정보이다. 
# 만약 0이라면 비어 있는 것이고, 1이라면 숲으로 막혀 있는 것이다. 

from collections import deque

n, m = map(int, input().split())
planet = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def convert_value_if_over_range(value, max_value):
    if value < 0:
        return max_value - 1
    elif value >= max_value:
        return 0
    else:
        return value

def bfs(row, col):
    q = deque()
    q.append((row, col))
    visited[row][col] = True

    while q:
        cur_row, cur_col = q.popleft()
        
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            new_row, new_col = cur_row + dx, cur_col + dy
            new_row = convert_value_if_over_range(new_row, n)
            new_col = convert_value_if_over_range(new_col, m)
    
            if not visited[new_row][new_col] and planet[new_row][new_col] == 0:
                q.append((new_row, new_col))
                visited[new_row][new_col] = True
    return 1

answer = 0
for row in range(n):
    for col in range(m):
        if planet[row][col] == 0 and not visited[row][col]:
            answer += bfs(row, col)

print(answer)