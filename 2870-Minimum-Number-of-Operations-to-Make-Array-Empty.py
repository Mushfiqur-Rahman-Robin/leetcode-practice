class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count_freq = collections.Counter(nums)
        
        operations_required = 0
        for key, val in count_freq.items():
            if val == 1:
                return -1
            else:
                operations_required += math.ceil(val / 3)
        
        return operations_required
