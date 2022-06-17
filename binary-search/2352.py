import sys
input = sys.stdin.readline

n = int(input())
array = [0] + list(map(int, input().split()))

memo = [0]
for num in array[1:]:
    if memo[-1] < num:
        memo.append(num)
    else:
        start = 0
        end = len(memo)

        while start < end:
            mid = (start + end) // 2

            if memo[mid] < num:
                start = mid + 1
            else:
                end = mid
        
        memo[end] = num

print(len(memo) - 1)