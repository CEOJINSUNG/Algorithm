import sys
input = sys.stdin.readline

n, m = map(int, input().split())
guitar = []
for _ in range(m):
    entire, individual = map(int, input().split())
    guitar.append((entire, individual))


six = sorted(guitar, key=lambda x : x[0])
one = sorted(guitar, key=lambda x : x[1])

answer = 0
if six[0][0] <= one[0][1] * 6:
    answer = six[0][0]*(n//6) + one[0][1] * (n%6)
    if six[0][0] < one[0][1] * (n%6):
        answer = six[0][0] * (n//6 + 1)
else:
    answer = one[0][1] * n

print(answer)