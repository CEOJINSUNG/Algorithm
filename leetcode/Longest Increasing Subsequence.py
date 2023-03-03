import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                index = bisect.bisect_left(dp, nums[i])
                dp[index] = nums[i]
        return len(dp)
        