class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_hay, len_need = len(haystack), len(needle)
        
        for i in range(len_hay - len_need + 1):
            if haystack[i:i+len_need] == needle:
                return i
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)