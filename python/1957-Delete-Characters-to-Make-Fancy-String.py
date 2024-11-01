class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for letter in s:
            if len(stack) > 1 and letter == stack[-1] == stack[-2]:
                stack.pop()
            stack.append(letter)
        
        return "".join(stack)

# In first iteration -> stack = [l]
# In second iteration -> stack = [l, e]
# In third iteration -> stack = [l, e, e]
# In fourth iteration -> stack = [l, e, e] -> after pop [l, e] -> after append [l, e, e]
# For other iterations it do not encounter pop.

    
# Time Complexity: O(n) — iterating through s once.
# Space Complexity: O(n) — storing up to n characters in stack.
