import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        def isNum(token: str) -> bool:
            if token in ["+", "-", "*", "/"]:
                return False
            return True
        
        for token in tokens:
            if isNum(token):
                nums.append(int(token))
            else:
                one = nums.pop()
                two = nums.pop()
                
                num = 0
                if token == "+":
                    num = one + two
                elif token == "-":
                    num = two - one
                elif token == "*":
                    num = one * two
                else:
                    num = math.trunc(two / one)
                nums.append(num)

        return nums[0]