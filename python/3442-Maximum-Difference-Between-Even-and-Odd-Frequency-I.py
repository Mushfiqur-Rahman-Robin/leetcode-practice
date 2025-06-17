class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = float("-inf")
        min_even = float("inf")

        if len(s) < 3:
            return 0

        freq_dict = collections.Counter(s)

        for elem in freq_dict.values():
            if elem % 2 != 0 and elem > max_odd:
                max_odd = elem
            elif elem % 2 == 0 and elem < min_even:
                min_even = elem
        
        return max_odd - min_even
        
        
# time complexity: O(n)
# space complexity: O(1)
