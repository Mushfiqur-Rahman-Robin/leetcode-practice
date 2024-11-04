class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        count = 1

        for i in range(1, len(word) + 1):
            if i < len(word) and word[i] == word[i - 1]:
                count += 1
            else:
                while count > 9:
                    comp += "9" + word[i - 1]
                    count -= 9

                comp += str(count) + word[i - 1]
                count = 1

        return comp
        

# Time Complexity: O(n) because we iterate through the string once.
# Space Complexity: O(n) for the result comp.
