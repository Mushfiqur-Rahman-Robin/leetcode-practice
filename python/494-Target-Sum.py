class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(idx, curr_sum):
            if (idx, curr_sum) in memo:
                return memo[(idx, curr_sum)]

            if idx == len(nums):
                return 1 if curr_sum == target else 0

                # if curr_sum == target:
                #     return 1
                # else:
                #     return 0
            
            memo[(idx, curr_sum)] = (
                backtrack(idx + 1, curr_sum + nums[idx]) +
                backtrack(idx + 1, curr_sum - nums[idx]))

            return memo[(idx, curr_sum)]
        
        return backtrack(0, 0)

# this is top-down dynamic programming approach with memorization
# tutorial link: https://www.youtube.com/watch?v=dwMOrl85Xes
# time complexity: O(n)
# space complexity: O(n)

