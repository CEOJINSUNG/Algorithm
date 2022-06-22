from itertools import combinations


n = int(input())
array = list(map(int, input().split()))

answer = 0
for i in combinations(array, 2):
    answer += (i[0]*i[1])

print(answer)