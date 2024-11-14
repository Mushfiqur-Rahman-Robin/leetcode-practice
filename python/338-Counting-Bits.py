class Solution:
    def countBits(self, n: int) -> List[int]:
        # O(n) solution
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            
            dp[i] = 1 + dp[i - offset]
        
        return dp


        # ans = [] # brute force solution

        # def set_bit_count(n):
        #     bit_count = 0
        #     for i in range(32):
        #         if (n >> i) & 1:
        #             bit_count += 1
        #     return bit_count
        
        # for num in range(0, n+1):
        #     ans.append(set_bit_count(num))
        
        # return ans

# Time Complexity: O(nlogn) due to counting bits for each number from 0 to n.
# Space Complexity: O(n) for storing the results in the ans list.
