class Solution:
    def smallestNumber(self, n: int) -> int:
        k = 1

        while (2**k - 1) < n:
            k += 1
        
        return 2**k - 1

# Time Complexity : O(log n), Loop increases `k` until 2^k ≥ n
# Space Complexity : O(1), Only constant extra variables used
# Check Note
