class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0 

        for i in range(len(str1)):
            if j == len(str2):
                return True

            if str1[i] == str2[j]:
                j += 1

            else:
                next_char = chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a'))
                if next_char == str2[j]:
                    j += 1

        return j == len(str2)    


# time complexity: O(n)
# space complexity: O(1)
# check note
