import sys

n, m = map(int, sys.stdin.readline().split())
city = []
house = []
chicken = []

for y in range(n):
    row = list(map(int, sys.stdin.readline().split()))

    for x in range(n):
        if row[x] == 1:
            house.append((x, y))
        elif row[x] == 2:
            chicken.append((x, y))
    
    city.append(row)

for home in house:
    min_distance = 200
    
    for store in chicken:
        distance = abs(home[0] - store[0]) + abs(home[1] - store[1])
        min_distance = min(min_distance, distance)
    

