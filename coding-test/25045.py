import sys

n, m = map(int, sys.stdin.readline().split())
satisfaction = list(map(int, sys.stdin.readline().split()))
costs = list(map(int, sys.stdin.readline().split()))

satisfaction.sort(reverse=True)
costs.sort()

answer = 0

for a, b in zip(satisfaction, costs):
    if a <= b:
        break
    answer += (a - b)

print(answer)