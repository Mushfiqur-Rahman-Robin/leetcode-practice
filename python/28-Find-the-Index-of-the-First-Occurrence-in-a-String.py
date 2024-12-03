class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        left = 0
        right = left + len(needle)

        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            left += 1
            right += 1
        
        return -1

# time complexity: O(n*m)
# space complexity: O(1)
