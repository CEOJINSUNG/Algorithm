n = int(input())
nums = list(map(int, input().split()))

m = int(input())
cards = list(map(int, input().split()))

nums.sort()

answer = []
for card in cards:
    start = 0
    end = len(nums) - 1

    exist = False
    while start <= end:
        mid = (start + end) // 2

        if nums[mid] > card:
            end = mid - 1
        elif nums[mid] < card:
            start = mid + 1
        else:
            exist = True
            break
    
    if exist:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)