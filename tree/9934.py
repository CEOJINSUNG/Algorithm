n = int(input())
array = list(map(int, input().split()))

answer = [[] for _ in range(n)]

def binary_tree(array, k):
    mid = (len(array) // 2)
    answer[k].append(array[mid])
    if len(array) == 1:
        return
    binary_tree(array[:mid], k+1)
    binary_tree(array[mid+1:], k+1)

binary_tree(array, 0)
for i in range(n):
    print(*answer[i])