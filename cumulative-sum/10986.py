from itertools import combinations

n, m = map(int, input().split())
array = list(map(int, input().split()))

div = [[] for _ in range(m)]
div[0] = [0]
num = 0
for i in array:
    num += i
    div[num%m].append(num)

answer = 0
for element in div:
    answer += len(list(combinations(element, 2)))

print(answer)