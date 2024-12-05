class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        return " ".join(reversed(word_list))

# time complexity: O(n)
# space complexity: O(n)
