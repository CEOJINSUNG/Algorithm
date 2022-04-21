import sys

student, color = map(int, sys.stdin.readline().split())
assign = []

for _ in range(color):
    num = int(sys.stdin.readline())
    assign.append(num)

left = 1
right = max(assign)

while left <= right:
    mid = (left + right) // 2

    total = 0
    for jewelry in assign:
        if jewelry % mid == 0:
            total += jewelry // mid
        else:
            total += (jewelry // mid) + 1
    
    if total > student:
        left = mid + 1
    else:
        right = mid - 1

print(left)