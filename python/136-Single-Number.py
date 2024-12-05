class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res = res ^ n   # n ^ 0 = n
        
        return res
        
