class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0

        for i in range(1, len(s), 2):
            if s[i] != s[i - 1]:
                changes += 1

        return changes

        
            
# Time Complexity: (O(n)), where (n) is the length of the string. The loop iterates once through half of the string's characters.
# Space Complexity: (O(1)), as only a few extra variables are used.

        

        
