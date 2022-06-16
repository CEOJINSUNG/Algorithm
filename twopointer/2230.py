import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

array.sort()

start = 0
end = 1

answer = 2*int(1e9) + 1
while start < n and end < n:
    value = array[end] - array[start]

    if value < m:
        if end == n-1:
            start += 1
        else:
            end += 1
    else:
        answer = min(answer, value)
        start += 1

print(answer)