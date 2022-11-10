from collections import deque

def bfs(x, y, board, answer):
    q = deque()
    q.append((x, y, board[y][x], 0, [(x, y)]))
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    m, n = len(board[0]), len(board)

    while q:
        cur_x, cur_y, word, index, visited = q.popleft()

        if word == answer:
            return True

        for i in range(4):
            new_x, new_y = cur_x + dx[i], cur_y + dy[i]

            if 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] == answer[index + 1] and (new_x, new_y) not in set(visited):
                new_word = word + answer[index + 1]
                if new_word == answer:
                    return True
                q.append((new_x, new_y, new_word, index + 1, visited + [(new_x, new_y)]))
    return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        coordinate = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    coordinate.append((j, i))
        
        for x, y in coordinate:
            if bfs(x, y, board, word):
                return True
        return False