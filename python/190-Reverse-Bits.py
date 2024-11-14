class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0

        # condensed version
        for _ in range(32):
            reversed_n = reversed_n << 1 | (n & 1)
            n >>= 1

        # for _ in range(32):
        #     reversed_n = reversed_n << 1
        #     bit = n & 1
        #     reversed_n =  reversed_n | bit
        #     n = n >> 1
        
        return reversed_n
            
# Tutorial link: https://www.youtube.com/watch?v=PywybHkTtPo
# time complexity is O(1)
# space complexity is O(1)
