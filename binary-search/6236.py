n, m = map(int, input().split())

money = [int(input()) for _ in range(n)]
start, end = 1, sum(money)

answer = 1
while start <= end:
    mid = (start + end) // 2
    charge = mid
    need = 1
    for i in money:
        if charge < i:
            charge = mid
            need += 1
        charge -= i
    
    if need > m or mid < max(money):
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)