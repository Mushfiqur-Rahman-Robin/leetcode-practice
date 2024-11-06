class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        def set_bit_count(num):
            return bin(num).count("1")

        cur_min, cur_max = nums[0], nums[0]
        prev_max = float("-inf")

        for n in nums:
            if set_bit_count(n) == set_bit_count(cur_min):
                cur_min = min(cur_min, n)
                cur_max = max(cur_max, n)
            else:
                if cur_min < prev_max:
                    return False
                prev_max = cur_max
                cur_min, cur_max = n, n
        
        if cur_min < prev_max:
            return False
        return True

# Tutorial link: https://www.youtube.com/watch?v=OpOPUeGFjxE
# Time complexity: O(n)
# Space complexity: O(1)

        
