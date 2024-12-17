class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)
        vowel_set = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'} # set checking is O(1) whereas list checking is O(n)

        while left < right:
            if s[left] not in vowel_set:
                left += 1
                continue # The continue statements ensure that the left and right pointers are only updated after confirming that both characters are vowels.
            if s[right] not in vowel_set:
                right -= 1
                continue
                
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return "".join(s)
    

# time complexity: O(n)
# space complexity: O(n)
# check note
