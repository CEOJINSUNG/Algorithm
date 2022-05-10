import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
answer = int(1e5)
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

for store in combinations(chicken, m):
    total = 0
    for home in house:
        each = 999
        for j in range(m):
            distance = abs(home[0] - store[j][0]) + abs(home[1] - store[j][1])
            each = min(each, distance)
        total += each
    answer = min(answer, total)

print(answer)