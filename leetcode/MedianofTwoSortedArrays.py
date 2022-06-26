import heapq
from bisect import bisect_left

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
        # 병합
        heap = nums1 + nums2
        
        # 힙 정렬 실행
        heapq.heapify(heap)
        
        # 길이 구함
        length = len(heap)
        middle = length // 2
        if length%2 == 1:
            for _ in range(middle):
                heapq.heappop(heap)
            return heapq.heappop(heap)
        else:
            for _ in range(middle-1):
                heapq.heappop(heap)
            one = heapq.heappop(heap)
            two = heapq.heappop(heap)
            return (one + two) / 2

# 다른 사람 풀이 1
def findMedianSortedArrays(self, nums1, nums2):
    a, b = sorted((nums1, nums2), key=len)
    m, n = len(a), len(b)
    after = (m + n - 1) // 2
    i = bisect_left(range(m), True, key=lambda i: after-i-1 < 0 or a[i] >= b[after-i-1])
    nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
    return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0

# 다른 사람 풀이 2
def findMedianSortedArrays(self, A, B):
    l = len(A) + len(B)
    if l % 2 == 1:
        return self.kth(A, B, l // 2)
    else:
        return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   
    
def kth(self, a, b, k):
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2 , len(b) // 2
    ma, mb = a[ia], b[ib]
    
    # when k is bigger than the sum of a and b's median indices 
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            return self.kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return self.kth(a[:ia], b, k)
        else:
            return self.kth(a, b[:ib], k)