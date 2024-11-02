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


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(list(set(nums)))

        if not nums_sorted:
            return 0

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == nums_sorted[i - 1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        return max(longest_streak, current_streak)


# Time Complexity: O(nlogn) due to sorting.
# Space Complexity: O(n) for storing the unique elements in sorted order.

