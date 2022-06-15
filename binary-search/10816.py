from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))

m = int(input())
card = list(map(int, input().split()))

nums.sort()

dict = defaultdict(int)
for num in nums:
    dict[num] += 1

final = []
for i in card:
    start = 0
    end = len(nums) - 1

    answer = False
    while start <= end:
        mid = (start + end) // 2

        if nums[mid] >= i:
            end = mid - 1
            if nums[mid] == i:
                answer = True
                break
        elif nums[mid] < i:
            start = mid + 1
    if answer:
        final.append(dict[i])
    else:
        final.append(0)

print(*final)