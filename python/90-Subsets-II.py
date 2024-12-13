class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                res.append(tmp[:])
                return
            
            tmp.append(nums[i]) # include the current number
            backtrack(i + 1)
            tmp.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]: # skip duplicates
                i += 1

            backtrack(i + 1) # exclude the current number

        backtrack(0)
        return res
        

# tutorial link: https://www.youtube.com/watch?v=Vn2v6ajA7U0
# time complexity: O(nlogn + 2^n⋅n)
# space complexity: O(n + 2^n⋅n)
# check note
