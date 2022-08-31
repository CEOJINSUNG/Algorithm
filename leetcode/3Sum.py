class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: 
            return []
        
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0: 
            return []

        ans = []
        for target in range(len(nums)-2):
            left, right = target+1, len(nums)-1

            if target > 0 and nums[target] == nums[target-1]:
                continue

            while left < right:
                total = nums[target] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[target], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return ans
        