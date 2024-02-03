class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                val_diff = abs(nums[i] - nums[j])
                index_diff = abs(j-i)

                if index_diff >= indexDifference and val_diff >= valueDifference:
                    return [i, j]
        return [-1, -1]

      
