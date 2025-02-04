class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]
        left = 0
        right = 1

        if len(nums) == 1:
            return nums[0]

        while right < len(nums):
            if nums[left] < nums[right]:
                curr_sum += nums[right]
                max_sum = max(max_sum, curr_sum)
                     
            else:
                curr_sum = nums[right]
            
            left = right 
            right += 1
        
        return max_sum


# time complexity: O(n)
# space complexity: O(1)
