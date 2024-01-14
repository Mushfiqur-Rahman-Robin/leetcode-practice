class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word_1_count = collections.Counter(word1)
        word_2_count = collections.Counter(word2)

        return (sorted(word_1_count.values()) == sorted(word_2_count.values()) and 
            sorted(word_1_count.keys()) == sorted(word_2_count.keys()))  
        
