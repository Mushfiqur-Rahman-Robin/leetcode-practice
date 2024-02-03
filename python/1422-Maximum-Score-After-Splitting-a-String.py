class Solution:
    def maxScore(self, s: str) -> int:
        elem_s = list(s)
        possible_ways = []

        for i in range(1, len(elem_s)):
            left, right = elem_s[:i], elem_s[i:]
            count_of_zeros = left.count('0')
            count_of_ones = right.count('1')

            possible_ways.append(count_of_zeros + count_of_ones)
        
        return max(possible_ways)
        
