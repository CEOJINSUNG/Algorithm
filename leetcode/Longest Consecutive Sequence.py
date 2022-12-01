import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = list(set(nums))
        heapq.heapify(nums)
        
        max_count = 1
        cur_num, cur_count = heapq.heappop(nums), 1
        while nums:
            num = heapq.heappop(nums)

            if num == cur_num + 1:
                cur_num = num
                cur_count += 1
                
                if cur_count > max_count:
                    max_count = cur_count
            else:
                cur_num = num
                cur_count = 1
        return max_count