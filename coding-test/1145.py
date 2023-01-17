nums = list(map(int, input().split()))

max_value = 100 * 100 * 100

cur_value = min(nums)
while cur_value < max_value:
    count = 0
    
    for num in nums:
        if cur_value%num == 0:
            count += 1
    
    if count >= 3:
        print(cur_value)
        break
    cur_value += 1