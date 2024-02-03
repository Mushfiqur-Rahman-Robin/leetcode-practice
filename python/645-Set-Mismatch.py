class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        for key, val in count.items():
            if val > 1:
                duplicate = key

        for i in range(1, len(nums)+1):
            if i not in nums:
                missing = i

        return [duplicate, missing]
        
