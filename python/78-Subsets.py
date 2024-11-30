class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        
        def dfs(i):
            if i == len(nums):
                res.append(tmp[:])
                return
            
            dfs(i + 1) # don't pick nums[i]

            tmp.append(nums[i]) # pick nums[i]
            dfs(i + 1)
            tmp.pop()

        dfs(0)
        return res      

# tutorial link: https://www.youtube.com/watch?v=UP3dOYJa05s
# time complexity: O(2^n)
# space complexity: O(n)
# check note
