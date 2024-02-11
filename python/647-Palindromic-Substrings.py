class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)
        for i in range(len(s)-1):
            for j in range(i + 1, len(s)):
                if s[i : j+1] == s[i : j+1][::-1]:
                    ans += 1

        return ans
        
# https://leetcode.com/problems/palindromic-substrings/solutions/4704298/easy-solution

# Time complexity O(n^3) (comparison also takes O(n) time)
# Space complexity O(1)
