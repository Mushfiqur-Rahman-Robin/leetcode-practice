class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split()
        word_mapping = {}

        if len(word_list) != len(pattern):
            return False
        
        for word, pattern_char in zip(word_list, pattern):
            if pattern_char in word_mapping:
                if word_mapping[pattern_char] != word:
                    return False
                
            elif word in word_mapping.values():
                return False

            word_mapping[pattern_char] = word
        
        return True
        
# time complexity: O(m + n^2)
# space complexity: O(n)
# check note
