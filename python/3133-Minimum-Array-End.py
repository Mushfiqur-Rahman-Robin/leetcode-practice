class Solution:
    def minEnd(self, n: int, x: int) -> int:
        i_x = 1
        i_n = 1
        res = x

        while i_n <= n - 1:
            if i_x & x == 0:
                if i_n & (n - 1):
                    res = res | i_x
                
                i_n = i_n << 1
            i_x = i_x << 1
        
        return res
        
# Check Note -> Must
        
# Tutorial link: https://www.youtube.com/watch?v=eA1xIDUqIDc, 
# https://www.youtube.com/watch?v=4pP-0UpEok4


# Step-by-Step Explanation
# Initialize Variables:


# i_x is initialized to 1, representing a bitmask to check individual bits of x starting from the least significant bit.
# i_n is initialized to 1, representing a bitmask to check bits of n-1.
# res is initialized to x. This will hold the result and is modified throughout the loop.

# While Loop: while i_n <= n - 1
# The loop continues as long as i_n is less than or equal to n-1. i_n is shifted left by one bit in each iteration, so it will eventually exceed n - 1.

# Bitwise Check of x: if i_x & x == 0
# This line checks if the bit in x at the current position (indicated by i_x) is not set (is 0).
# If the condition is true (meaning the bit in x at the current i_x position is 0), we proceed to the next step.

# Bitwise Check of n - 1: if i_n & (n - 1)
# This checks if the bit in n - 1 at the position indicated by i_n is set (is 1).
# If this bit in n - 1 is 1, it performs a bitwise OR operation on res with i_x to set that specific bit in res.

# Left Shift i_n: i_n = i_n << 1
# After updating res, we left-shift i_n to move to the next higher bit in the next iteration.

# Left Shift i_x: i_x = i_x << 1
# i_x is also left-shifted in each iteration to move to the next bit position in x.
# Return res: return res

# After the loop completes, the function returns the final value of res, which has been modified based on the bits in x and n.

# Summary of the Logic
# The function seems to be modifying res (initially set to x) by checking each bit position. If a bit in x is not set and the corresponding bit in n - 1 is set, it sets the bit in res at that position. This process continues until all bits up to n - 1 have been checked.
# Essentially, this function is selectively setting bits in res based on the binary structure of x and n - 1.






