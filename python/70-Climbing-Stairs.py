class Solution:
    def climbStairs(self, n: int) -> int:
        p2, p1 = 0, 1

        for i in range(n):
            p2, p1 = p1, (p1+p2)
        return p1
        

# Initialization: Initialize two variables p2 and p1 to represent the number of ways to climb to the current step and the next step, respectively. Initially, p2 is set to 0, and p1 is set to 1.

# Loop through steps: Use a for loop to iterate through each step from 0 to n - 1. The loop index i represents the current step.

# Update variables: Inside the loop, update p2 and p1 based on the number of ways to reach the current step and the next step. The update is done using tuple unpacking, swapping the values of p2 and p1, and assigning the new values.

# p2, p1 = p1, (p1 + p2)
# Here's how the values are updated in each iteration:

# Initial: p2=0, p1=1
# 1st iteration: p2=1, p1=(1+0)=1
# 2nd iteration: p2=1, p1=(1+1)=2
# 3rd iteration: p2=2, p1=(2+1)=3
# ... and so on.
# Return result: After the loop, return the final value of p1. This represents the total number of distinct ways to climb to the top of the stairs.

# Now, let's say n is the total number of steps in the stairs. The final value of p1 after the loop will be the number of distinct ways to climb to the top of the stairs with n steps. The algorithm efficiently computes this by updating the number of ways at each step based on the previous two steps.
