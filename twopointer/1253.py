n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
answer = 0

# 궁금한점 정렬을 하고 오른쪽 열은 왜 받아야 하는 것인가
for i in range(n):
    temp = numbers[:i] + numbers[i+1:]
    left, right = 0, len(temp)-1

    while left < right:
        t = temp[left] + temp[right]
        if t == numbers[i]:
            answer += 1
            break
        
        if t < numbers[i]: left += 1
        else: right -= 1

print(answer)
# good = defaultdict(set)
# good_total = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         value = numbers[i] + numbers[j]
#         if value > max_value:
#             break

#         if value in good:
#             continue

#         if value in set(numbers) and value not in good:
#             first_index = numbers.index(value)
#             if first_index not in good[value]:
#                 for next in range(first_index, n):
#                     if numbers[next] == value:
#                         good[value].add(next)
#                         good_total += 1
#                     else:
#                         break

# print(good_total)