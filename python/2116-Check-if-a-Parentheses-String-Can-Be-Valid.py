class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        total_brackets = len(s)

        # If the total number of brackets is odd, it's impossible to balance
        if total_brackets % 2 != 0:
            return False

        # Forward pass: Check '(' balance
        open_count = 0
        free_count = 0
        for i in range(total_brackets):
            if locked[i] == '0':  # Unlocked character
                free_count += 1
            elif s[i] == '(':
                open_count += 1
            else:  # s[i] == ')'
                if open_count > 0:
                    open_count -= 1
                elif free_count > 0:
                    free_count -= 1
                else:
                    return False

        # Backward pass: Check ')' balance
        close_count = 0
        free_count = 0
        for i in range(total_brackets - 1, -1, -1):
            if locked[i] == '0':  # Unlocked character
                free_count += 1
            elif s[i] == ')':
                close_count += 1
            else:  # s[i] == '('
                if close_count > 0:
                    close_count -= 1
                elif free_count > 0:
                    free_count -= 1
                else:
                    return False

        return True

# tutorial link: https://www.youtube.com/watch?v=D00qGvqmqN0
# time complexity: O(n)
# space complexity: O(1)
