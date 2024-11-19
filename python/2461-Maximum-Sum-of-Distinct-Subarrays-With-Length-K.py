class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        curr_sum = 0
        l = 0
        count_freq = defaultdict(int)

        for r in range(len(nums)):
            curr_sum += nums[r]
            count_freq[nums[r]] += 1

            if r - l + 1 > k:
                count_freq[nums[l]] -= 1
                if count_freq[nums[l]] == 0:
                    del count_freq[nums[l]]

                curr_sum -= nums[l]
                l += 1
            
            if r - l + 1 == k and len(count_freq) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum

# time complexity: O(n)
# space complexity: O(k)
# check note
