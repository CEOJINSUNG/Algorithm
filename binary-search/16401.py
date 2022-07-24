m, n = map(int, input().split())
snack = list(map(int, input().split()))

left, right = 0, max(snack)
answer = 0
while left <= right:
    mid = (left + right) // 2
    count = 0

    if mid == 0:
        count = 0
        break
    
    for i in snack:
        if i >= mid:
            count += (i // mid)
            
    if count >= m:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)