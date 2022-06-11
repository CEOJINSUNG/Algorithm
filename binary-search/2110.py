import sys
input =  sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

start = 1
end = house[-1] - house[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    router = house[0]
    temp = int(1e9)

    for i in range(1, n):
        if router + mid <= house[i]:
            temp = min(house[i]-router, temp)
            count += 1
            router = house[i]
    
    if count < c:
        end = mid - 1
    else:
        start = mid + 1
        answer = max(answer, temp)
    
print(answer)