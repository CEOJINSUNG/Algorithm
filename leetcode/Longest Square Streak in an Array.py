class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        answer = -1
        nums.sort()

        temp = set(nums)
        for num in nums:
            if num not in temp:
                continue

            count = 1
            while num * num in temp:
                count += 1
                temp.remove(num)
                num = num * num
            
            if count > 1 and count > answer:
                answer = count
        return answer