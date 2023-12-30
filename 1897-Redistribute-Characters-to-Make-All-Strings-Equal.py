from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = Counter("".join(words))
        len_words = len(words)
        for val in count.values():
            if val % len_words != 0:
                return False
        return True
        
