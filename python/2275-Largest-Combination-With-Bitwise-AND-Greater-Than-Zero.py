class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0

        for i in range(32):
            cnt = 0
            for n in candidates:
                if n & (1 << i):
                    cnt += 1

            res = max(res, cnt)

        return res

# Time Complexity: O(n)
# Space Complexity: O(1)
