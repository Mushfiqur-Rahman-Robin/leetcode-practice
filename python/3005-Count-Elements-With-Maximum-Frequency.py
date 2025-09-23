class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        total_count = 0
        freq_distribution = Counter(nums)
        max_of_freq = max(freq_distribution.values())
        
        for v in freq_distribution.values():
            if v == max_of_freq:
                total_count += max_of_freq
        
        return total_count

# time complexity: O(n)
# space complexity: O(unique)
