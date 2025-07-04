class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_at_indexes = []
        res = []

        for i in range(len(nums)):
            if nums[i] == key:
                key_at_indexes.append(i)
        
        for i in range(len(nums)):
            for j in range(len(key_at_indexes)):
                if abs(i - key_at_indexes[j]) <= k:
                    res.append(i)
                    break
        
        return res
        
# Time complexity: O(n∗m)
# Space complexity: O(n)
