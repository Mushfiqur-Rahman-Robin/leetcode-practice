class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        valid_split_cnt = 0
        left_sum = 0
        total_sum = sum(nums)

        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total_sum - left_sum

            if left_sum >= right_sum:
                valid_split_cnt += 1
        
        return valid_split_cnt

# time complexity: O(n)
# space complexity: O(1)
