class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        total_word_with_prefix = 0

        for w in words:
            if w.startswith(pref):
                total_word_with_prefix += 1
        
        return total_word_with_prefix
    
# time complexity: O(n * len(pref))
# space complexity: O(1)
