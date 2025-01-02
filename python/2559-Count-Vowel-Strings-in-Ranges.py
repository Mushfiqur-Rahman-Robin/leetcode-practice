class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        
        def is_vowel_str(word):
            return word[0] in vowel_set and word[-1] in vowel_set

        n = len(words)
        prefix_sum = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + (1 if is_vowel_str(words[i - 1]) else 0)
            
        for l, r in queries:
            res.append(prefix_sum[r+1] - prefix_sum[l])

        return res

        
# time complexity: O(n)
# space complexity: O(n)
# check note
