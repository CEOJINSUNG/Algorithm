import sys

n = int(sys.stdin.readline())
village = []
total = 0

for _ in range(n):
    x, a = map(int, sys.stdin.readline().split())
    village.append([x, a])
    total += a

village.sort()

temp = 0
for i in range(n):
    temp += village[i][1]
    if (temp >= (total+1)//2):
        print(village[i][0])
        break