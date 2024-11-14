class Solution:
    def getSum(self, a: int, b: int) -> int:
        # a is sum without carry
        # b is carry
        mask = 0xffffffff
        while (mask & b) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        
        return (mask & a) if b > 0 else a
    
# Separation of carry Calculation:

# By first calculating carry = (a & b) << 1, you store the carry result before updating a with a = a ^ b.
# This separation ensures that b (the carry) is isolated and only updated with the correct carry bits after a is modified.

# tutorial link: https://www.youtube.com/watch?v=MmIx_NrCkGI
# Time Complexity: O(1), due to the fixed 32-bit integer constraint.
# Space Complexity: O(1), due to constant auxiliary memory usage.
