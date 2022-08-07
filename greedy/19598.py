import sys, heapq
input = sys.stdin.readline

n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]
work.sort()

answer = 1
room = [0]
for s, e in work:
    if s >= room[0]:
        heapq.heappop(room)
    else:
        answer += 1
    heapq.heappush(room, e)

print(answer)