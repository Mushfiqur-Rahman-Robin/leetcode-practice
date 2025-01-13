class Solution:
    def minimumLength(self, s: str) -> int:
        deletions = 0
        char_freq = {}

        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        for count in char_freq.values():
            if count % 2 == 0:
                deletions += (count - 2)
            else:
                deletions += (count - 1)
        
        return len(s) - deletions


# tutorial link: https://leetcode.com/problems/minimum-length-of-string-after-operations/solutions/6271294/simple-even-odd-count-detailed-explanation
# time complexity: O(n)
# space complexity: O(1)
        
