class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        answer = 0
        stack = [] 
        heights = [0] + heights + [0]
        
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                j = stack.pop()
                answer = max(answer, (i - stack[-1] - 1) * heights[j])
            stack.append(i)
        return answer