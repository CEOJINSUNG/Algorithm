from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        answer = [[]]
        for i in range(1, len(nums)):
            for element in combinations(nums, i):
                answer.append(list(element))
        
        answer.append(nums)
        return sorted(answer)
        