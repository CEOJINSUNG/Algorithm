board = [list(map(int, input().split())) for _ in range(5)]

number = set()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    string = str(board[y][x])
    q = []
    q.append((x, y, string))

    while q:
        cur_x, cur_y, cur_string = q.pop()

        if len(cur_string) == 6:
            number.add(cur_string)
            continue

        for i in range(4):
            new_x, new_y = cur_x + dx[i], cur_y + dy[i]

            if 0 <= new_x < 5 and 0 <= new_y < 5:
                q.append((new_x, new_y, cur_string + str(board[new_y][new_x])))

for i in range(5):
    for j in range(5):
        dfs(j, i)

print(len(number))