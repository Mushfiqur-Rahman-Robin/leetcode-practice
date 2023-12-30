class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        obtained_list = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if len(nums[i:j+1]) >= 1:
                    obtained_list.append(len(set(nums[i:j+1]))**2)

        return sum(obtained_list)
