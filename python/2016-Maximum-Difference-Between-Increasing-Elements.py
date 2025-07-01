class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = float("-inf")
        criteria_holds = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] - nums[i] <= 0:
                    continue
                else:
                    max_diff = max(max_diff, nums[j] - nums[i])
                    criteria_holds += 1
        
        return max_diff if criteria_holds > 0 else -1
            

# Time Complexity: O(n²)
# Space Complexity: O(1)
