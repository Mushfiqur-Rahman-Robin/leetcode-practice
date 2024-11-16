class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0

        for i in range(len(s)):
            l, r = i, i # odd length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1

                l -= 1
                r += 1

            l, r = i, i + 1 # even length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1

                l -= 1
                r += 1
        
        return res

# tutorial link: https://www.youtube.com/watch?v=XYQecbcd6_c
# Time Complexity: O(n ^ 2)
# Space Complexity: O(1), as no additional data structures proportional to n are used.
