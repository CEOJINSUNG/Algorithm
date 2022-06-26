from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
nums = [i for i in range(n)]
a, b = [], []
for _ in range(n):
    flavorA, flavorB = map(int, input().split())
    a.append(flavorA)
    b.append(flavorB)

answer = int(1e9)
for i in range(1, n+1):
    for element in combinations(nums, i):
        tempA, tempB = 1, 0
        for index in element:
            tempA *= a[index]
            tempB += b[index]
        if answer > abs(tempA - tempB):
            answer = abs(tempA - tempB)

print(answer)