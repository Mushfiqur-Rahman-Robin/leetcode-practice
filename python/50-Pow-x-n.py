class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def func(base = x, exponent = abs(n)):
            if exponent == 0:
                return 1
            if exponent % 2 == 0:
                return func(base * base, exponent // 2)
            else:
                return base * func(base * base, (exponent - 1) // 2)
        
        return func() if n >= 0 else 1 / func()

# solution link: https://leetcode.com/problems/powx-n/solutions/749109/python-recursive-solution-faster-than-99

# time complexity: O(logn)
# space complexity: O(logn)
