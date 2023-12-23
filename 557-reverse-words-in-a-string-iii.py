class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([elem[::-1] for elem in s.split(' ')])
        
