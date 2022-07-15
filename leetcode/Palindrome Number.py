class Solution:
    def isPalindrome(self, x: int):
        x = str(x)
        length = len(x)
        left, right = 0, length - 1
        
        check = True
        while left < right:
            if x[left] != x[right]:
                check = False
                break
            else:
                left += 1
                right -= 1
        return check