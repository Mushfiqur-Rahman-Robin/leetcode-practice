class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            # Avoid duplicates for the first element in the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Set up two pointers for the two-sum part
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers and avoid duplicates for the second and third elements
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result

# Time: O(n^2)
# Space: O(n) (Excluding the output)
# Solution tutorial: https://www.youtube.com/watch?v=TBePcj8DgxM
