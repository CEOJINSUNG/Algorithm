n = int(input())
array = list(map(int, input().split()))

total = sum(array)
answer = 0
for i in array:
    total -= i
    answer += i*total

print(answer)