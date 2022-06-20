t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    cumulative = [0] * n
    cumulative[0] = array[0]
    for i in range(1, n):
        cumulative[i] = max(cumulative[i-1]+array[i], array[i])
    
    print(max(cumulative))