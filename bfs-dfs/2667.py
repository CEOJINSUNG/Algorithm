from collections import deque
import sys

n = int(sys.stdin.readline())
house = []
for _ in range(n):
    house.append(list(sys.stdin.readline().strip()))

def bfs(column, row):
    global number
    result = 1

    d_column = [-1, 1, 0, 0]
    d_row = [0, 0, -1, 1]

    q = deque()
    q.append((column, row))
    house[column][row] = "0"

    while q:
        current_column, current_row = q.popleft()

        for i in range(4):
            new_column, new_row = current_column + d_column[i], current_row + d_row[i]

            if 0 <= new_column < n and 0 <= new_row < n and house[new_column][new_row] == "1":
                result += 1
                house[new_column][new_row] = "0"
                q.append((new_column, new_row))
    
    return result

if n == 1:
    if house[0][0] == "1":
        print(1)
        print(1)
    else: 
        print(0)
else:
    number_of_house = []
    for i in range(n):
        for j in range(n):
            if house[i][j] == "1":
                number_of_house.append(bfs(i, j))

    number_of_house.sort()

    print(len(number_of_house))
    for i in number_of_house:
        print(i)