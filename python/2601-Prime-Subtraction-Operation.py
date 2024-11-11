class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prev = 0  # Initialize `prev` to 0 since the first element has no prior element
        for i in range(len(nums)):
            # Find the largest prime `p` such that `nums[i] - p > prev`
            largest_p = self.largest_prime_smaller_than_upper_bound(nums[i], prev)
            
            # If after adjustments, the current number is not greater than the previous, return False
            if nums[i] - largest_p <= prev:
                return False
            
            nums[i] -= largest_p
            prev = nums[i]  # Update prev to the current number for the next comparison

        return True

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def largest_prime_smaller_than_upper_bound(self, n, prev):
        upper_bound = n - prev  # Calculate the upper bound for the largest prime we can subtract
        for i in range(upper_bound - 1, 1, -1):
            if self.is_prime(i):
                return i
        return 0
    

    
