class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i+1:] + s[:i+1] == goal:
                return True
        return False

# Time Complexity: O(n) 
# Space Complexity: O(n)

# Another solution:

# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         return len(s) == len(goal) and goal in s + s
#  if s = "abcde", then s + s = "abcdeabcde" contains all rotations: "abcde", "bcdea", "cdeab", "deabc", "eabcd".
