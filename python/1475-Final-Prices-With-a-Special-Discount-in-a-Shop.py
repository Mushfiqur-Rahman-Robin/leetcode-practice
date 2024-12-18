class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        left = 0
        right = 1

        while left < len(prices):
            if right < len(prices) and prices[left] >= prices[right]:
                prices[left] = prices[left] - prices[right]
                left += 1
                right = left + 1

            elif right < len(prices) and prices[left] < prices[right]:
                right += 1
            
            else:
                left += 1
                right = left + 1
        
        return prices
    

# time complexity: O(n^2)
# space complexity: O(1)
# check note for optimized solution using monotonic stack
