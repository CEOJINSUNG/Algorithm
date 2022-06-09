from itertools import combinations
import sys

n, s = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(1, n+1):
    array = combinations(num, i)
    for j in array:
        if sum(j) == s:
            answer += 1

print(answer)