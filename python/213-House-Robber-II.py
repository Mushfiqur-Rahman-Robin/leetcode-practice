class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.house_robber_basic(nums[1:]), \
            self.house_robber_basic(nums[:-1]))
        

    def house_robber_basic(self, nums):
        n = len(nums)
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2]+ nums[i], dp[i - 1])

        return dp[n-1]

# Tutorial link: https://www.youtube.com/watch?v=Aivg_MSs2w4
# Time complexity: O(n)
# Space complexity: O(n)
