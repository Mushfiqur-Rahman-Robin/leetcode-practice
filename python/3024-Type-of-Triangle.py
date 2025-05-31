class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort(reverse=True)
        
        if nums[0] >= nums[1] + nums[2]:
            return "none"
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"
        else:
            return "scalene"
        
# Time Complexity: O(1)
# Space Complexity: O(1)
