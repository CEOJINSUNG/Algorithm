def twoSum(self, nums: List[int], target: int):
        remain = dict()
        
        for i, num in enumerate(nums):
            if (target-num) in remain:
                return [i, remain[target-num]]
            else:
                remain[num] = i