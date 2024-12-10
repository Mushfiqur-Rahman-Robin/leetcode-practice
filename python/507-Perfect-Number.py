class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 6, 28, 496, 8128, 33550336
        sum_of_divisors = 1

        if num <= 1:
            return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                sum_of_divisors += i
                if i != num // i:
                    sum_of_divisors += num // i 
                
        return sum_of_divisors == num
    
# time complexity: O(root(n))
# space complexity: O(1)
# check note
