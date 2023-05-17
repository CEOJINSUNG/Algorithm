from collections import deque

def solution(board):
    col, row = len(board), len(board[0])
    
    dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
    start_col, start_row = 0, 0
    for i in range(col):
        for j in range(row):
            if board[i][j] == "R":
                start_col, start_row = i, j
                break
    
    visited = [[-1] * row for _ in range(col)]
    q = deque()
    q.append((start_row, start_col))
    visited[start_col][start_row] = 0
    
    while q:
        cur_row, cur_col = q.popleft()
        
        if board[cur_col][cur_row] == "G":
            return visited[cur_col][cur_row]
        
        for i in range(4):
            new_r, new_c = cur_row, cur_col
            
            while True:
                new_c += dc[i]
                new_r += dr[i]
                
                if 0 <= new_c < col and 0 <= new_r < row and board[new_c][new_r] == "D":
                    new_c -= dc[i]
                    new_r -= dr[i]
                    break
                
                if new_c < 0 or new_c >= col or new_r < 0 or new_r >= row:
                    new_c -= dc[i]
                    new_r -= dr[i]
                    break
            
            if visited[new_c][new_r] == -1:
                visited[new_c][new_r] = visited[cur_col][cur_row] + 1
                q.append((new_r, new_c))

    return -1