import sys
from itertools import combinations

n = int(sys.stdin.readline())

num = []
for i in range(1, 11):
    for j in combinations(range(0, 10), i):
        j = list(j)
        j.sort(reverse=True)
        num.append(int("".join(map(str, j))))

num.sort()

try:
    print(num[n])
except:
    print(-1)