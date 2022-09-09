import sys
input = sys.stdin.readline

n = int(input())
a = input().split(" ")
a = [int(i) for i in a]

sorted_a = [i for i in a]
sorted_a.sort()

p = []
for i in a:
    p.append(sorted_a.index(i))
    sorted_a[sorted_a.index(i)] = -1

print(*p)
