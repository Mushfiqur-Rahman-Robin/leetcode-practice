class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_ops = 0
        greater_than_k = set()

        for num in nums:
            if num < k:
                return -1
            if num > k and num not in greater_than_k:
                min_ops += 1
                greater_than_k.add(num)

        return min_ops

# time complexity: O(n)
# space complexity: O(n)
# tutorial link: https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/solutions/6631158/array-hash-table-o-n

