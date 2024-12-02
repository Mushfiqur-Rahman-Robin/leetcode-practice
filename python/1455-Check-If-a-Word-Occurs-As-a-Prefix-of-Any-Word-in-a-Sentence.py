class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        res = float("inf")
        words = sentence.split(" ")
        for index, words in enumerate(words):
            if words.startswith(searchWord):
                return index + 1
        
        return -1
        
# time complexity: O(n)
# space complexity: O(n)
