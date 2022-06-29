x, y = map(int, input().split())

if x == y:
    print(-1)
else:
    init = (y*100)//x
    start, end = 1, x
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        current = ((y+mid)*100)//(x+mid)
        
        if current > init:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    
    if answer == 0: print(-1)
    else: print(answer)