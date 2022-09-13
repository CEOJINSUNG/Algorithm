class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for string in s:
            if len(stack) == 0:
                stack.append(string)
            elif stack[-1] == "[" and string == "]":
                stack.pop()
            elif stack[-1] == "(" and string == ")":
                stack.pop()
            elif stack[-1] == "{" and string == "}":
                stack.pop()
            else:
                stack.append(string)
        
        if len(stack) != 0:
            return False
        return True
        