class Solution:
    def isHappy(self, n: int) -> bool:
        def do_square(n):
            squared_sum = 0
            for num in str(n):
                squared_num = int(num) ** 2
                squared_sum += squared_num

            return squared_sum
        
        seen = set()
        
        while n != 1:
            if n in seen:
                return False  # We have a cycle, so return False
            seen.add(n)
            n = do_square(n)
        
        return True

# time complexity: O(logn)
# space complexity: O(logn)
# check note

# For optimal space complexity, we can use Floyd’s Tortoise and Hare cycle detection algorithm, which reduces space complexity to O(1) without needing to store all previous numbers. This would not improve time complexity but could significantly optimize space usage.
