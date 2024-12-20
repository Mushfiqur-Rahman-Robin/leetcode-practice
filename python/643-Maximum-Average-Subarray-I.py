class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        curr_sum = sum(nums[left:right])
        max_sum = curr_sum

        while right < len(nums):
            curr_sum = curr_sum + nums[right] - nums[left]
            max_sum = max(curr_sum, max_sum)

            left += 1
            right += 1
        
        return round(max_sum / k, 5)


# time complexity: O(n)
# space complexity: O(1)
# check note
