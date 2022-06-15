n = int(input())
array = [0] + list(map(int, input().split()))

memoization = [0]

for num in array[1:]:
    if memoization[-1] < num:
        memoization.append(num)
    else:
        left = 0
        right = len(memoization)

        while left < right:
            mid = (left + right) // 2

            if memoization[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        memoization[right] = num

print(len(memoization) - 1)