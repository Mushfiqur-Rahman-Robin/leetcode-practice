class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            min_coin = float('inf')

            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                min_coin = min(min_coin, dp[diff] + 1)
            
            dp[i] = min_coin

        
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1

# tutorial link: https://www.youtube.com/watch?v=koE9ly1CFDc
# Time complexity: O(coin * amount)
# Space complexity: O(amount)
