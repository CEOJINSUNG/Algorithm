from copy import deepcopy


n = int(input())
honey = list(map(int, input().split()))
another_honey = deepcopy(honey)

for i in range(1, n):
    honey[i] += honey[i-1]

answer = 0
for i in range(1, n-1):
    answer = max(answer, 2*honey[-1] - another_honey[0] - another_honey[i] - honey[i])

for i in range(1, n-1):
    answer = max(answer, honey[-1] - another_honey[-1] - another_honey[i] + honey[i-1])

for i in range(1, n-1):
    answer = max(answer, honey[i] - another_honey[0] + honey[-1] - honey[i-1] - another_honey[-1])

print(answer)