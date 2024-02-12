class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_freq = collections.Counter(nums)
        rule_of_majority = len(nums) / 2

        for key, val in count_freq.items():
            if val >= rule_of_majority:
                return key
        
