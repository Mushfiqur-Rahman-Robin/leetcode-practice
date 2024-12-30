class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = {}
        mod = 10**9 + 7

        def backtrack(length):
            if length > high:
                return 0
            
            if length in dp:
                return dp[length]

            dp[length] = 1 if length >= low else 0
            dp[length] += backtrack(length + zero) + backtrack(length + one)

            return dp[length] % mod

        return backtrack(0)


# tutorial link: https://www.youtube.com/watch?v=QQoIiY4K-M0
# time complexity: O(high)
# space complexity: O(high)
# check note
