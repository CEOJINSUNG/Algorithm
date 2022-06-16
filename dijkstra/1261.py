import heapq
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

miro = [list(input().strip()) for _ in range(n)]

visited = [[int(1e9)]*m for _ in range(n)]
def dijkstra(x, y):
    h = []
    heapq.heappush(h, (0, x, y))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while h:
        cur_count, cur_x, cur_y = heapq.heappop(h)
        if cur_x == m-1 and cur_y == n-1:
            continue

        for i in range(4):
            new_x = cur_x + dx[i]
            new_y = cur_y + dy[i]

            if 0 <= new_x < m and 0 <= new_y < n:
                if visited[new_y][new_x] == int(1e9):
                    if miro[new_y][new_x] == "1":
                        visited[new_y][new_x] = cur_count + 1
                        heapq.heappush(h, (cur_count+1, new_x, new_y))
                    else:
                        visited[new_y][new_x] = cur_count
                        heapq.heappush(h, (cur_count, new_x, new_y))

dijkstra(0, 0)
print(visited[n-1][m-1])