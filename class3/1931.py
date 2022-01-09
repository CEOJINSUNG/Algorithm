N = int(input())

meeting = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))

count, end = 0, 0

for i in meeting:
    if i[0] >= end:
        count += 1
        end = i[1]

print(count)