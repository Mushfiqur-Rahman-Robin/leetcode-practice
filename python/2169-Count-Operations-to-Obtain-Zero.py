class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        total_operations = 0

        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            total_operations += 1

        return total_operations

