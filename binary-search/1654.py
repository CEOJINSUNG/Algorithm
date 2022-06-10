import sys
input = sys.stdin.readline

k, n = map(int, input().split())

max_length = 0
loop = []
for _ in range(k):
    element = int(input())
    loop.append(element)
    
start = 1
end = max(loop)

while start <= end:
    mid = (start+end) // 2
    count = 0

    for element in loop:
        num = element // mid
        count += num

    if count >= n:
        start = mid + 1
    elif count < n:
        end = mid - 1

print(end)