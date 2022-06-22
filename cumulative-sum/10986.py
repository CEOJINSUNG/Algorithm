n, m = map(int, input().split())
array = list(map(int, input().split()))

div = [0 for _ in range(m)]
div[0] = 1
num = 0
for i in array:
    num += i
    div[num%m] += 1

answer = 0
for element in div:
    answer += (element * (element - 1) //2)

print(answer)