class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_elem = set()

        max_length = 0
        left = 0

        for right in range(len(s)):
            while s[right] in unique_elem:
                unique_elem.remove(s[left])
                left += 1
            unique_elem.add(s[right])

            max_length = max(max_length, right - left + 1)
    
        return max_length
            

# https://www.youtube.com/watch?v=wiGpQwVHdE0

# Time complexity O(n)
# Space complexity O(n)
