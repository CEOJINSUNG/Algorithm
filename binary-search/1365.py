n = int(input())
array = list(map(int, input().split()))

dp = [array[0]]
for num in array[1:]:
    if dp[-1] < num:
        dp.append(num)
    else:
        left, right = 0, len(dp)

        while left < right:
            mid = (left + right) // 2

            if dp[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        dp[right] = num

print(n - len(dp))