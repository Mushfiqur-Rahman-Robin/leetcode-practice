class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        far = 0 
        smallest = 0
        
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])

            if i == end:
                smallest += 1
                end = far
        
        return smallest


# tutorial link: https://www.youtube.com/watch?v=CsDI-yQuGeM
# time complexity: O(n)
# space complexity: O(1)
# check note


