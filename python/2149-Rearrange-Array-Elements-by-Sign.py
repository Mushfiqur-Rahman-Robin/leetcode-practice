class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = 0
        r = 1

        res = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                res[l] = nums[i]
                l += 2
            if nums[i] < 0:
                res[r] = nums[i]
                r += 2
        
        return res

# https://www.youtube.com/watch?v=SoPmcGzz9-E

# Time complexity O(n)
        
