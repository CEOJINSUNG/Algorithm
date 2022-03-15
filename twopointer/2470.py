import sys

N = int(input())
liquid = list(map(int, input().split()))

liquid.sort()

left = 0
right = N-1

special = liquid[left] + liquid[right]
two_liquid = [liquid[left], liquid[right]]

while left < right:
    two_special = liquid[left] + liquid[right]

    if abs(two_special) < abs(special):
        special = two_special
        two_liquid = [liquid[left], liquid[right]]

        if special == 0:
            break
    
    if two_special < 0:
        left += 1
    else:
        right -= 1

print(*sorted(two_liquid))