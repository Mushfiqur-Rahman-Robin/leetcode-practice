class Solution: # optimized version by chatgpt
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        min_ops = 0
        start = 0

        while start < n:
            remaining = nums[start:]
            if len(remaining) == len(set(remaining)):
                break
            min_ops += 1
            start += 3
        
        return min_ops

# Time Complexity: O(n)
# Space Complexity: O(n)

# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         min_ops = 0
        
#         while len(nums) > len(set(nums)):
#             nums = nums[3:]
#             min_ops += 1

#         return min_ops

# Time Complexity: O(n^2)
# Space Complexity: O(n)
