class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # word_list = s.split(" ")
        # word_list = [elem for elem in word_list if elem != ""]
        word_list = [elem for elem in s.split(" ") if elem]
        
        return len(word_list[-1]) if word_list else 0
