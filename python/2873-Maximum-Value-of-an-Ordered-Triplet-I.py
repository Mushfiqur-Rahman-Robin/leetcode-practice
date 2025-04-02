class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_res = 0
        max_val = nums[0]
        max_diff = 0

        if len(nums) < 3:
            return 0
        
        for i in range(1, len(nums)):
            max_res = max(max_res, max_diff * nums[i])

            max_diff = max(max_diff, max_val - nums[i])

            max_val = max(max_val, nums[i])
    
        return max_res


# time complexity: O(n)
# space complexity: O(1)
# tutorial: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/solutions/6605299/brute-force-best-solution-optimal-triplet-value-with-greedy-prefix-diff-in-one-pass

        
