class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, num in enumerate(numbers):
            if target - num in dictionary:
                return [dictionary[target-num]+1, i+1]
            dictionary[num] = i