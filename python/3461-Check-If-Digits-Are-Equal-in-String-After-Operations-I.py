class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(s)
        length = len(s)

        while (length > 2):
            for i in range(length - 1):
                s[i] = str( (int(s[i]) + int(s[i+1])) % 10 )
                # print(s[i],s)
            length -= 1
        
        return s[0] == s[1]

# Time complexity: O(n^2), where n is the length of s
# Space complexity: O(n), where n is the length of s
