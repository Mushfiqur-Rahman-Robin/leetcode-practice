class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for index, value in enumerate(nums):
            difference = target - value
            if difference in dictionary:
                return [dictionary[difference], index]
            dictionary[value] = index
        return
                    

# Time Complexity: O(n)
# Space Complexity: O(n)
# Tutorial: https://www.youtube.com/watch?v=KLlXCFG5TnA
