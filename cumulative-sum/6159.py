import sys
input = sys.stdin.readline

n, s = map(int, input().split())
cow = [int(input()) for _ in range(n)]
cow.sort()

count = 0
for i in range(n-1):
    for j in range(i+1, n):
        if cow[i] + cow[j] <= s:
            count += 1
print(count)