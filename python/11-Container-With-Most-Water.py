class Solution:
    def maxArea(self, height: List[int]) -> int:
        # this brute force approach works but causes time limit exceeded in leetcode

        # max_water = 0
        # for i in range(0, len(height)):
        #     for j in range(i + 1, len(height)):
        #         min_height = min(height[i], height[j])
        #         max_water = max((min_height * (j - i)), max_water)
        
        # return max_water

        # time complexity O(n^2)
        # space complexity O(n^2)

        # Linear solution

        max_water = 0

        l, r = 0, len(height) - 1

        while (l < r):
            area = min(height[l], height[r]) * (r - l)
            max_water = max(max_water, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_water
            
# https://www.youtube.com/watch?v=UuiTKBwPgAo
