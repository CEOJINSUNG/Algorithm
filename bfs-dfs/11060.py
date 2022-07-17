from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
miro = list(map(int, input().split()))

visited = [10000]*n

q = deque()
q.append((0, 0, miro[0]))
visited[0] = 0

while q:
    count, position, jump = q.popleft()

    for next in range(1, jump + 1):
        next_position = position + next
        if next_position < n:
            if visited[next_position] == 10000:
                q.append((count + 1, next_position, miro[next_position]))
                visited[next_position] = count + 1

print(visited[n-1] if visited[n-1] != 10000 else -1)