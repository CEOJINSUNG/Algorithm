students = [input() for _ in range(5)]
princess = [[0]*5 for _ in range(5)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[0]*5 for _ in range(5)]
answer = 0

q = []

def check(position):
    global visited
    x = position%5
    y = position//5

    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]

        if 0 <= new_x < 5 and 0 <= new_y < 5:
            if visited[new_y][new_x] == 0:
                if (new_y*5+new_x) in q:
                    visited[new_y][new_x] = 1
                    check((new_y*5+new_x))

def dfs(count, index, y_num):
    global answer
    global visited

    if y_num >= 4 or 25 - index < 7 - count:
        return
    
    if count == 7:
        check(q[0])
        if sum(sum(visited, [])) == 7:
            answer += 1
        visited = [[0]*5 for _ in range(5)]
        return
    
    x = index%5
    y = index//5

    q.append(index)
    if students[y][x] == "Y":
        dfs(count+1, index+1, y_num+1)
    else:
        dfs(count+1, index+1, y_num)
    
    q.pop()
    dfs(count, index+1, y_num)

dfs(0, 0, 0)
print(answer)
