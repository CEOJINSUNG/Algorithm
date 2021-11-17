from itertools import combinations


n, m = map(int, input().split())
arr = list(map(int, input().split()))
max_len = 0

for i in range(len(arr)):
    arr[i] = arr[i]%m

for i in range(1, n+1):
    for j in combinations(arr, i):
        if sum(j)%m == m-1:
            max_len = sum(j)%m
            break
        if (sum(j)%m) > max_len:
            max_len = sum(j)%m