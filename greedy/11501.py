import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    value, max = 0, 0

    for i in range(len(nums)-1,-1,-1):
        if(nums[i] > max):
            max = nums[i]
        else:
            value += max-nums[i]
    
    print(value)