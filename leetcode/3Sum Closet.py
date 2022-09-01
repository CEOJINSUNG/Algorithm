class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = 1e5
        
        nums.sort()
        for index, cur in enumerate(nums):
            left, right = index + 1, len(nums) - 1
            while left < right :
                three_sum = cur + nums[left] + nums[right]
                if abs(target - three_sum) < abs(diff):
                    diff = target - three_sum
                
                if three_sum > target:
                    right -= 1
                else:
                    left += 1
                
            if diff == 0 :
                break
                
        return target - diff