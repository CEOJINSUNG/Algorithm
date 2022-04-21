n, m, l = map(int, input().split())
road = list(map(int, input().split()))
road.append(0)
road.append(l)
road.sort()

left = 1
right = l
answer = 0

while left <= right:
    count = 0
    mid = (left + right)//2

    for i in range(1, len(road)):
        if (road[i] - road[i-1]) > mid:
            count += (road[i] - road[i-1] - 1)//mid
    
    if count > m:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)