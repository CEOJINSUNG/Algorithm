import sys, heapq
input = sys.stdin.readline

n = int(input())
matrix = [list(input()) for _ in range(n)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
way = []
visited = [[False]*n for _ in range(n)]
heapq.heappush(way, (0, 0, 0))

while way:
    black, x, y = heapq.heappop(way)

    if x == n-1 and y == n-1:
        print(black)
        break

    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < n and visited[new_y][new_x] == False:
            visited[new_y][new_x] = True
            if matrix[new_y][new_x] == "0":
                heapq.heappush(way, (black+1, new_x, new_y))
            else:
                heapq.heappush(way, (black, new_x, new_y))