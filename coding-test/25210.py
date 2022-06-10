n = int(input())
array = list(map(int, input().split()))

min_value = []
for i in array:
    if len(min_value) == 0:
        min_value.append(i)
    else:
        if i < min_value[-1]:
            min_value.append(i)
        else:
            min_value.append(min_value[-1])

current_distance = 0
max_value = array[0]
max_index = 0
answer = [0]
for i in range(1, n):
    num = array[i]
    if num - min_value[i-1] >= current_distance:
        max_value = num
        max_index = i
        current_distance = num - min_value[i-1]
        answer.append(current_distance)
    else:
        answer.append(current_distance)

print(*answer)