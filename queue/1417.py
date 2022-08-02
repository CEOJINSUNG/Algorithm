import sys
input = sys.stdin.readline

n = int(input())
d = int(input())
vote = [int(input()) for _ in range(n-1)]
vote.sort(reverse=True)

answer = 0
if n == 1:
    print(answer)
else:
    while vote[0] >= d:
        d += 1
        vote[0] -= 1
        answer += 1
        vote.sort(reverse=True)
    print(answer)
