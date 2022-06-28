n, k = map(int, input().split())
array = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    array[i] += array[i-1]

answer = -10001
for i in range(n-k+1):
    value = array[i+k] - array[i]
    if answer < value:
        answer = value
print(answer)