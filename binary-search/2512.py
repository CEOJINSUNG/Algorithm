n = int(input())
nums = list(map(int, input().split()))
nation = int(input())

total = sum(nums)

if nation >= total:
    print(max(nums))
else:
    start = 1
    end = max(nums)
    answer = 0

    while start < end:
        mid = (start + end) // 2

        cost = 0
        for num in nums:
            if mid <= num:
                cost += mid
            else:
                cost += num

        if cost > nation:
            end = mid
        else:
            start = mid + 1
            answer = max(answer, mid)
    print(answer)