from collections import deque


n, m = map(int, input().split())

war = [list(input()) for _ in range(m)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = {"W": 0, "B": 0}
def bfs(x, y, word):
    q = deque()
    q.append((x, y))
    war[y][x] = "F"
    count = 1

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            new_x, new_y = cur_x + dx[i], cur_y + dy[i]

            if 0 <= new_x < n and 0 <= new_y < m and war[new_y][new_x] == word:
                war[new_y][new_x] = "F"
                count += 1
                q.append((new_x, new_y))
    answer[word] += count**2

for i in range(m):
    for j in range(n):
        if war[i][j] == "W":
            bfs(j, i, "W")
        if war[i][j] == "B":
            bfs(j, i, "B")

print(str(answer["W"]) + " " + str(answer["B"]))