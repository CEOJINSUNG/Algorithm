import itertools, math

T = int(input())

for _ in range(T):
    N = int(input())
    point = []
    sum_x = 0
    sum_y = 0

    for _ in range(N):
        x, y = map(int, input().split())
        point.append((x, y))
        sum_x += x
        sum_y += y
    
    vector = list(itertools.combinations(point, int(N/2)))
    answer = float("inf")
    
    for i in vector[:int(len(vector)/2)]:
        sum_x1 = 0
        sum_y1 = 0

        for x1, y1 in list(i):
            sum_x1 += x1
            sum_y1 += y1
        
        sum_x2 = sum_x - sum_x1
        sum_y2 = sum_y - sum_y1

        answer = min(answer, math.sqrt(
            (sum_x1 - sum_x2) ** 2 + (sum_y1 - sum_y2) ** 2
        ))
    
    print(answer)
