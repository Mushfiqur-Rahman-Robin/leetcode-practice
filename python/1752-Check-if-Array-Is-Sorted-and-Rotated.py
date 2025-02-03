class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        if n == 1:
            return True

        for i in range(1, 2 * n):
            if nums[(i - 1) % n] <= nums[i % n]:
                count += 1
            else:
                count = 1
            
            if count == n:
                return True
        
        return False

# tutorial link: https://www.youtube.com/watch?v=Vzs_vlCIFEw
# time complexity: O(n)
# space complexity: O(1)
