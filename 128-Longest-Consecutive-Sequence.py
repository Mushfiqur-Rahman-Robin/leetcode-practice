class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_len = 0

        num_set = set(nums)

        for n in nums:
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                
                longest_len = max(length, longest_len)
        
        return longest_len


# Time complexity O(n)
# Space complexity O(n)
