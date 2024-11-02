class Solution:
    def isPalindrome(self, s: str) -> bool:
        plain_str = ''.join([char for char in s if char.isalnum()]).lower()
        
        return plain_str == plain_str[::-1]
        

## Time complexity: Total Time Complexity: O(n)
## Space complexity: Total Space Complexity: O(n)
