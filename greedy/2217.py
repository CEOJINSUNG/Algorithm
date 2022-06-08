import sys

n = int(sys.stdin.readline())
rope = []
for _ in range(n):
    rope.append(int(sys.stdin.readline()))

rope.sort(reverse=True)

answer = 0
for i in range(n):
    count = i + 1
    weight = rope[i]
    if count * weight > answer:
        answer = count*weight

print(answer)