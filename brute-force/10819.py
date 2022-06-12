from itertools import permutations

n = int(input())
array = list(map(int, input().split()))

brute = list(permutations(array, n))

max_value = 0
for element in brute:
    temp = 0
    for i in range(0, len(element)-1):
        temp += abs(element[i] - element[i+1])
    max_value = max(max_value, temp)

print(max_value)