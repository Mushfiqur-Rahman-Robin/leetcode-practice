class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for prime in [2, 3, 5]:
            while n % prime == 0: 
                n = n // prime
        
        return n == 1

# tutorial link: https://www.youtube.com/watch?v=M0Zay1Qr9ws
# time complexity: O(logn)
# space complexity: O(1)
# check note
