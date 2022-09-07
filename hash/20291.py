from collections import defaultdict
import sys
input = sys.stdin.readline

file = defaultdict(int)

n = int(input())
for _ in range(n):
    file[input().strip().split(".")[1]] += 1

for data in sorted(file.items(), key=lambda x: x[0]):
    print(*data)