class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort() # O(nlogn)
        res = []

        for i in range(0, len(nums), 3): # O(n)
            if nums[i+2] - nums[i] > k:
                return []
            res.append(nums[i: i+3])
        
        return res

# https://www.youtube.com/watch?v=XleOio1oJeo
