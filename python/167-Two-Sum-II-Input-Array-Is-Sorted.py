class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            
            if numbers[left] + numbers[right] > target:
                right -= 1
            
            if numbers[left] + numbers[right] < target:
                left += 1
            

# tutorial link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/solutions/5101915/video-using-two-pointers-to-solve-the-question-with-o-1-space     
# time complexity: O(n)
# space complexity: O(1)

        
