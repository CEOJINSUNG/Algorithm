class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        # 해당 높이에 존재하는 요소들의 개수를 최대로 늘리면 
        # 최소로 제거해야하는 요소를 찾을 수 있음
        beans.sort()
        length = len(beans)
        max_value = max([(length - index) * height for index, height in enumerate(beans)])
        return sum(beans) - max_value