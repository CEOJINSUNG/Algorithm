n, m = map(int, input().split())
array = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    array[i] += array[i-1]

left, right = 0, m
answer = 0
while left < right:
    if right == n+1:
        right -= 1
    
    temp = array[right] - array[left]
    if temp > answer:
        answer = temp
    left += 1
    right += 1

print(answer)