k, n = map(int, input().split())
array = list(map(int, input().split()))

count = 1
num = array[0] * count + abs(array[0]-k)
while True:
    check = True
    for i in range(1, n-1, 2):
        first = array[i]*count + abs(array[i]-k)
        second = array[i+1]*count + abs(array[i+1]-k)
        if first == second:
            num = first
        else:
            check = False
            break
    
    if check:
        print(count)
        break
    count += 1