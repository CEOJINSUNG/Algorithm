class Solution:
    def isMatch(self, s, p):
        if not p: return not s
        if not s: return len(p) > 1 and p[1] == '*' and self.isMatch(s, p[2:])
        Matched = (p[0] == '.' or p[0] == s[0])
        if len(p) > 1 and p[1] == '*':
            return (Matched and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        return Matched and self.isMatch(s[1:], p[1:])