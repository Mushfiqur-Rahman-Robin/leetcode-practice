class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_so_far = 0
        lowest_price_so_far = prices[0]

        for current_price in prices[1:]:
            if current_price < lowest_price_so_far:
                lowest_price_so_far = current_price

            current_profit = current_price - lowest_price_so_far

            max_profit_so_far = max(max_profit_so_far, current_profit)

        return max_profit_so_far


# Time complexity O(n)
# Space complexity O(1)
