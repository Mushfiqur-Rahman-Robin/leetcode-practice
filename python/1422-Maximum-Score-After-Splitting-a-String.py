class Solution:
    def maxScore(self, s: str) -> int:
        max_score = float('-inf')
        zero_count = 0
        one_count = s.count('1')

        # Stop before the last character to ensure non-empty substrings
        for i in range(len(s) - 1):
            if s[i] == '0':
                zero_count += 1
            
            elif s[i] == '1':
                one_count -= 1

            max_score = max(max_score, zero_count + one_count)

        return max_score

            
# time complexity: O(n)
# space complexity: O(1)
# check note
