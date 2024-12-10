class Solution:
    def maximumLength(self, s: str) -> int:
        freq_count = {}
        max_len = -1

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(set(s[i:j])) == 1: #  to check if the substring consists of only one unique character
                    freq_count[s[i:j]] = 1 + freq_count.get(s[i:j], 0)
        
        for key, val in freq_count.items():
            if val >= 3:
                max_len = max(max_len, len(key))

        return max_len      

# time complexity: O(n^3)
# space complexity: O(n^2)
# this is the worst time and space complexity. there is a room for optimization.
