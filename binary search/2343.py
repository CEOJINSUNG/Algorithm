N, M = map(int, input().split())

length = list(map(int, input().split()))

left, right = max(length), sum(length)

answer = 0

while left <= right:
    mid = (left + right) // 2
    current_total = 0
    current_count = 0

    for i in length:
        if current_total + i > mid:
            current_count += 1
            current_total = i
        else:
            current_total += i
    
    if current_count <= M - 1:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
