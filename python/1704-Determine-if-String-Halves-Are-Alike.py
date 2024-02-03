class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        s = s.lower()
        count_left = 0
        count_right = 0
        vowel = ['a', 'e', 'i', 'o', 'u']

        text_left = s[:len(s)// 2]
        text_right = s[len(s)// 2:]
        
        for elem in vowel:
            count_left += text_left.count(elem)
            count_right += text_right.count(elem)
        
        return count_left == count_right
        
