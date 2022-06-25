import sys
input = sys.stdin.readline

# 1차 풀이
# from bisect import bisect_left, bisect_right
# n, h = map(int, input().split())
# number = [0]*h

# for i in range(n):
#     height = int(input())
#     if i%2 == 0:
#         for j in range(h-1, h-height-1, -1):
#             number[j] += 1
#     else:
#         for j in range(height):
#             number[j] += 1

# number.sort()
# min_value = number[0]
# def count_by_range(array, left_value, right_value):
#     right_index = bisect_right(array, right_value)
#     left_index = bisect_left(array, left_value)
#     return right_index - left_index

# print(min_value, count_by_range(number, min_value, min_value))

# 2차 풀이
n, h = map(int, input().split())
top = [0] * (h+1)
bottom = [0] * (h+1)

for i in range(n):
    height = int(input())
    if i%2 == 0:
        bottom[h-height+1] += 1
    else:
        top[height] += 1
    
for i in range(h-1, 0, -1):
    top[i] += top[i+1]

for i in range(1, h+1):
    bottom[i] += bottom[i-1]

total = [0]*(h+1)
for i in range(1, h+1):
    total[i] = top[i] + bottom[i]

answer = min(total[1:])
print(answer, total[1:].count(answer))