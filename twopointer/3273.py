n = int(input())
array = list(map(int, input().split()))
x = int(input())
array.sort()
left, right = 0, n-1
answer = 0

while left < right:
    temp = array[left] + array[right]
    if temp == x:
        answer += 1
    elif temp < x:
        left += 1
        continue
    right -= 1

print(answer)