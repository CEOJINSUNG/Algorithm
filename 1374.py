from heapq import heappush, heappop

n = int(input())
lecture = [list(map(int, input().split())) for _ in range(n)]

lecture.sort(key=lambda x: (x[1], x[2]))

answer = 1
cur_lecture = [lecture[0][2]]

for num, start, end in lecture[1:]:
    if cur_lecture[0] <= start:
        heappop(cur_lecture)
        heappush(cur_lecture, end)
    else:
        heappush(cur_lecture, end)
    answer = max(len(cur_lecture), answer)

print(answer)