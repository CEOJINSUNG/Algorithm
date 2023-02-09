class Solution:
    def findType(self, low, high, answer):
        # 짝수끼리 있는 경우
        if (low%2 == 0 and high%2 == 0) or (high%2 == 0 and low%2 == 1):
            return answer
        return answer + 1
        
    def countOdds(self, low: int, high: int) -> int:
        return self.findType(low, high, high // 2 - low // 2)