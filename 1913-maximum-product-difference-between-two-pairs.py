class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        max_prod_diff = (nums[0] * nums[1]) - (nums[len(nums)-1] * nums[len(nums)-2])
        return max_prod_diff
