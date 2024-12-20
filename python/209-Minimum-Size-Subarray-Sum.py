class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_subarr_sum = 0
        min_subarr_len = float('inf')

        for right in range(len(nums)):
            curr_subarr_sum += nums[right]

            while curr_subarr_sum >= target:
                min_subarr_len = min(min_subarr_len, right - left + 1)
                curr_subarr_sum -= nums[left]
                left += 1

        return min_subarr_len if min_subarr_len != float('inf') else 0

# time complexity: O(n)
# space complexity: O(1)
# check note 
