class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_freq_one_index = []
        char_freq = collections.Counter(s)

        for key, val in char_freq.items():
            if val == 1:
                position = s.index(key)
                char_freq_one_index.append(position)

        if char_freq_one_index:
            return min(char_freq_one_index)
        return -1
