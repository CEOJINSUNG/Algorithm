class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        
#         answer = [-1, -1]
#         while left<=right:
#             mid = (left + right) // 2
            
#             if nums[mid] == target:
#                 if nums[right] != target: 
#                     right -= 1
#                 if nums[left] != target:
#                     left += 1
                    
#                 answer = [left, right]
#                 break
#             elif nums[mid]>target:
#                 right = mid-1
#             else:
#                 left = mid+1
        
        # print(answer)
        # if len(answer) < 2:
        #     answer = [left, left]
        
        temp = []
        for index in range(len(nums)):
            if nums[index] == target:
                temp.append(index)
            elif nums[index] > target:
                break
                
        if len(temp) > 0:
            return [temp[0], temp[-1]]
        return [-1, -1]