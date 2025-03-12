class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        max_count_pos = 0
        max_count_neg = 0

        for num in nums:
            if num < 0:
                max_count_neg += 1
            if num > 0:
                max_count_pos += 1
            else:
                continue
        
        return max(max_count_pos, max_count_neg)

# time complexity: O(n)
# space complexity: O(1)

