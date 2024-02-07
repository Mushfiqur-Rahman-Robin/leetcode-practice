class Solution:
    def frequencySort(self, s: str) -> str:
        count_freq = collections.Counter(s)
        sorted_count_freq = sorted(count_freq.items(), key=lambda x: x[1], reverse=True)

        res = ''
        for pair in sorted_count_freq:
            res += (pair[0] * pair[1]) 
        
        return res
