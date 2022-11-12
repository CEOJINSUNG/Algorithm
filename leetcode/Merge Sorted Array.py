class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
        
        # answer = []
        # one, two = 0, 0
        
        # while one < m and two < n:
        #     if nums1[one] < nums2[two]:
        #         answer.append(nums1[one])
        #         one += 1
        #     else:
        #         answer.append(nums2[two])
        #         two += 1
        
        # if one < m:
        #     for i in range(one, m):
        #         answer.append(nums1[i])
        # elif two < n:
        #     for i in range(two, n):
        #         answer.append(nums2[i])
        
        # nums1 = answer
