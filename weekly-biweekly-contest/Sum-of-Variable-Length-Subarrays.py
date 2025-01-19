class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        i = 0
        res = 0

        while i < len(nums):
            start = max(0, i - nums[i])
            res += sum(nums[start:i+1])
            i += 1

        return res

# time complexity: O(n^2)
# space complexity: O(1)©leetcode
