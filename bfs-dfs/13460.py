from collections import deque
import copy

n, m = map(int, input().split())

a_board = [list(input()) for _ in range(n)]
b_board = copy.deepcopy(a_board)

# arrow will include up: 0, down: 1, right: 2, left: 3
arrow = []

# x means horizontal and y means vertical in sequence up, down, right, left
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def bfs(x, y, graph):
    q = []
    q.append([(x, y)])

    while q:
        path = q.pop(0)
        graph[y][x] = 0

        current_x, current_y = path[-1]

        if graph[current_y][current_x] == 'O':
            previous_x, previous_y = path[-2]
            graph[current_y][current_x] = graph[previous_y][previous_x]
            for k in range(len(graph)):
                print(*graph[k])
            return path
        
        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if 0 < next_x < m-1 and 0 < next_y < n-1 and (graph[next_y][next_x] == "." or graph[next_y][next_x] == "B" or graph[next_y][next_x] == "O"):
                if graph[next_y][next_x] == 'O':
                    graph[next_y][next_x] = "O"
                # elif graph[next_y][next_x] != 'O':
                #     graph[next_y][next_x] = "#"
                elif len(arrow) == 0:
                    #push the way of marble
                    arrow.append(i)
                        
                    # Change the Basic position to 1
                    # . -> 1
                    graph[next_y][next_x] = 1
                
                # if previous way is the same as current way, maintain it
                elif arrow[-1] == i:
                    graph[next_y][next_x] = graph[current_y][current_x]
                
                # if previous way is diffrent from current way, increase the number of way
                elif arrow[-1] != i:
                    graph[next_y][next_x] = graph[current_y][current_x] + 1
                    arrow.append(i)
                
                new_path = list(path)
                new_path.append((next_x, next_y))
                q.append(new_path)
    
    return -1

for i in range(n):
    for j in range(m):
        if a_board[i][j] == "R":
            print(bfs(j, i, a_board))
        # if b_board[i][j] == "B":
        #     print(bfs(j, i, b_board))

print(arrow)