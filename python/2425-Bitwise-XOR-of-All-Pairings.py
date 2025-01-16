class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        
        if len(nums2) % 2 == 1:
            for n in nums1:
                res ^= n

        if len(nums1) % 2 == 1:
            for m in nums2:
                res^= m

        return res  

# tutorial link: https://www.youtube.com/watch?v=H9zVwDf6Frk
# time complexity: O(n)
# space complexiy: O(1)
