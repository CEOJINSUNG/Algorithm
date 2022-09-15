import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        num = dividend/divisor
        if num < 0:
            num = math.ceil(num)
            return min(max(-2147483648, num), 2147483647) 
        num = math.floor(num)
        return min(max(-2147483648, num), 2147483647) 