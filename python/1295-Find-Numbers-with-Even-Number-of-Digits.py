class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        num_with_even_digits_cnt = 0

        for n in nums:
            if len(str(n)) % 2 == 0:
                num_with_even_digits_cnt += 1
        
        return num_with_even_digits_cnt

# Time Complexity: O(n × log m)
# Space Complexity: O(1)   
