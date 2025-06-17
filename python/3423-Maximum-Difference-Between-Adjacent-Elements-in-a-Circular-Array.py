class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        first_elem = nums[0]
        last_elem = nums[-1]

        max_diff = abs(first_elem - last_elem)

        for i in range(len(nums)-1):
            max_diff = max(max_diff, abs(nums[i] - nums[i+1]))
        
        return max_diff

# Time Complexity: O(n)
# Space Complexity: O(1)
