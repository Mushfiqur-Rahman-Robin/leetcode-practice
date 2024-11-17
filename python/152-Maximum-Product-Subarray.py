class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = nums[0]
        min_p = nums[0]
        maximum_product = max_p

        for i in nums[1:]:
            temp = min_p
            min_p = min(i, min_p * i, max_p * i)
            max_p = max(i, temp * i, max_p * i)

            maximum_product = max(maximum_product, max_p)

        return maximum_product

        
# tutorial link: https://www.youtube.com/watch?v=eiJf3AjbCRk
# time complexity: O(n)
# space complexity: O(1)
