class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # more optimized version
        elem_freq = Counter(nums)
        sorted_freq = sorted(nums, key = lambda x: (elem_freq[x], -x))
        return sorted_freq

        # time complexity: O(nlogn)
        # space complexity: O(k)


        # initial version
        # elem_freq = {}
        # res = []

        # for elm in nums:
        #     elem_freq[elm] = 1 + elem_freq.get(elm, 0)
        
        # sorted_elem_freq = dict(sorted(elem_freq.items(), key=lambda x: (x[1], -x[0])))

        # for key, val in sorted_elem_freq.items():
        #     res += [key] * val
        
        # return res

# time complexity: O(n + klogk)
# space complexity: O(n + k)
# check note


        
