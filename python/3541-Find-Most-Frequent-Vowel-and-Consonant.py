class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = set("aeiou")
        consonant = set("bcdfghjklmnpqrstvwxyz")

        max_freq_vowel = 0
        max_freq_consonant = 0

        count_freq = Counter(s)
        
        for key, val in count_freq.items():
            if key in vowel:
                max_freq_vowel = max(max_freq_vowel, val)
            if key in consonant:
                max_freq_consonant = max(max_freq_consonant, val)

        return max_freq_vowel + max_freq_consonant

# time complexity: O(n)
# space complexity: O(1)
        
