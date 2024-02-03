class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        concat_s = (s+s)[1:-1]
        return s in concat_s
