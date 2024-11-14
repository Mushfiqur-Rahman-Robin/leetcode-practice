class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # more optimized
        n = len(nums)
        expected_sum = n * (n+1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
        # Time Complexity: O(n)
        # Space Complexity: O(1)


        # return sum(list(range(0, len(nums)+1))) - sum(nums)
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
