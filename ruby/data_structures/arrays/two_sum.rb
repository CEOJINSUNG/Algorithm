def two_sum(nums, target)
    result_array = []

    nums.count.times do |i|
        nums.count.times do |j|
            next unless i != j && i < j
            
            current_sum = nums[i] + nums[j]
            return [i, j] if current_sum == target
        end
    end
end

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6), "\n")

def two_sum(nums, target)
    nums.each_with_index do |num, i|
        target_differennce = target - num

        nums.each_with_index do |num, j|
            return [i, j] if i != j && num == target_differennce
        end
    end
end

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6), "\n")

# 아래는 two pointer인데 주어진 배열이 정렬된 상태임
def two_sum(nums, target)
    left, right = 0, nums.length - 1
    
    while left < right
        sum = nums[left] + nums[right]

        if target < sum
            right -= 1
        elsif target > sum
            left += 1
        else 
            return [left + 1, right + 1]
        end
    end
end

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([2, 3, 4], 6))
print(two_sum([-1, 0], -1))