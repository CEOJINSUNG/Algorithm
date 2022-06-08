import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

p.sort()

total = 0
temp = 0
for i in p:
    temp += i
    total += temp

print(total)