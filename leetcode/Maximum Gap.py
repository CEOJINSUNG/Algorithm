class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        return max([nums[i + 1] - nums[i] for i in range(len(nums) - 1)]) if len(nums) > 1 else 0