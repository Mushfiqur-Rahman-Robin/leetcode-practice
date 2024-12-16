class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        while k > 0:
            min_of_nums = min(nums)
            idx_of_min = nums.index(min_of_nums)
            nums[idx_of_min] *= multiplier
            k -= 1

        return nums 

# time complexity: O(n)
# space complexity: O(1)
# check note

        
