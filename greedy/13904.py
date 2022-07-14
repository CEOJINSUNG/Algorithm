import sys
input = sys.stdin.readline

n = int(input())
index, final = 0, 0
assign = [list(map(int, input().split())) for _ in range(n)]
assign.sort(reverse=True, key=lambda x: x[1])

answer = [0]*1001
for i in range(n):
    for j in range(assign[i][0]-1, -1, -1):
        if answer[j] == 0:
            answer[j] = assign[i][1]
            break

print(sum(answer))