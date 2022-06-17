import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()

target = 1
for num in array:
    if target < num:
        break
    target += num

print(target)