class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                res[stack_index] = i - stack_index
            stack.append([t, i])

        return res

# https://www.youtube.com/watch?v=cTBiBSnjO3c

# Time complexity O(n)
# Space complexity O(n) and an extra stack with O(n)
         

# Let's review the process with the example temperatures list [73, 74, 75, 71, 69, 72, 76, 73]. Here's how the res (result list) and stack change in each step:

# Initial State:

# res = [0, 0, 0, 0, 0, 0, 0, 0]
# stack = []
# No warmer day found yet, so everything is zero.
# After Processing 73 (temperatures[0]):

# res = [0, 0, 0, 0, 0, 0, 0, 0]
# stack = [[73, 0]]
# 73 is added to the stack as no warmer day is found.
# After Processing 74 (temperatures[1]):

# res = [1, 0, 0, 0, 0, 0, 0, 0]
# stack = [[74, 1]]
# 74 is warmer than 73, so we update res[0] to 1 (one day until a warmer temperature) and replace 73 with 74 in the stack.
# After Processing 75 (temperatures[2]):

# res = [1, 1, 0, 0, 0, 0, 0, 0]
# stack = [[75, 2]]
# 75 is warmer than 74, so res[1] is set to 1. Now, 75 is on the stack.
# After Processing 71 (temperatures[3]):

# res = [1, 1, 0, 0, 0, 0, 0, 0]
# stack = [[75, 2], [71, 3]]
# 71 is not warmer than 75, so it's just added to the stack.
# After Processing 69 (temperatures[4]):

# res = [1, 1, 0, 0, 0, 0, 0, 0]
# stack = [[75, 2], [71, 3], [69, 4]]
# 69 is cooler, so it's added to the stack.
# After Processing 72 (temperatures[5]):

# res = [1, 1, 0, 2, 1, 0, 0, 0]
# stack = [[75, 2], [72, 5]]
# 72 is warmer than 71 and 69 but not 75, so we update res[3] and res[4] accordingly, and add 72 to the stack.
# After Processing 76 (temperatures[6]):

# res = [1, 1, 4, 2, 1, 1, 0, 0]
# stack = [[76, 6]]
# 76 is warmer than all previous, so we update res[2], res[3], res[4], and res[5]. The stack is now only holding 76.
# After Processing 73 (temperatures[7]):

# res = [1, 1, 4, 2, 1, 1, 0, 0]
# stack = [[76, 6], [73, 7]]
# 73 is not warmer than 76, so it's added to the stack.
# The final res list [1, 1, 4, 2, 1, 1, 0, 0] tells you how many days you would have to wait until a warmer temperature for each corresponding day
