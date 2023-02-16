class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # 정렬된 배열이 존재함
        # 해당 요소를 가지고 나누기를 진행함
        # 진행해서 정렬하였을 때
        # k 번째 존재하는 요소를 찾음
        if len(arr) == 2:
            return arr

        array = []
        length = len(arr)
        for left in range(length - 1):
            for right in range(left + 1, length):
                array.append((arr[left] / arr[right], arr[left], arr[right]))
        
        array.sort()
        return [array[k - 1][1], array[k - 1][2]]