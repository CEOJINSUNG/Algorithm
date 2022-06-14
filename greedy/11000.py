import heapq
import sys
input = sys.stdin.readline

n = int(input())
teacher = []
for i in range(n):
    teacher.append(list(map(int, input().split())))

teacher.sort(key=lambda x: (x[0], x[1]))
room = []
heapq.heappush(room, teacher[0][1])

for i in range(1, n):
    if teacher[i][0] < room[0]:
        heapq.heappush(room, teacher[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, teacher[i][1])

print(len(room))