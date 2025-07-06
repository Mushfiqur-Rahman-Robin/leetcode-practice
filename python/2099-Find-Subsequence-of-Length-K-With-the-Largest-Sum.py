class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        largest_sum = nums[:k]

        for n in nums[k:]:
            min_ans_val = min(largest_sum)

            if n > min_ans_val:
                largest_sum.remove(min_ans_val)
                largest_sum.append(n)
        
        return largest_sum


# time complexity: O(n*m)
# space complexity: O(1)
