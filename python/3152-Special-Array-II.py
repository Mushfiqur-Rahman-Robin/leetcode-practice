class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        is_alternating = [False] * (n - 1)

        for i in range(n-1):
            is_alternating[i] = (nums[i] % 2 != nums[i + 1] % 2)
        
        prefix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + (1 if i - 1 < len(is_alternating) and is_alternating[i - 1] else 0)

        res = []
        for start, end in queries:
            num_of_alternating_pairs = prefix_sum[end] - prefix_sum[start]
            total_pairs = end - start
            res.append(num_of_alternating_pairs == total_pairs)

        return res
            

# time complexity: O(n+q)
# space complexity: O(n+q)
# check note
