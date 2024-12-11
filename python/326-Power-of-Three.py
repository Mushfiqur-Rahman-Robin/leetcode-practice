class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n // 3
        return n == 1
        
        # for x in range(32):
        #     if 3 ** x == n:
        #         return True
        
        # return False
        
