class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_sum = -1
        num_sum_map = defaultdict(list)

        for n in nums:
            digit_sum = sum(int(d) for d in str(n))
            num_sum_map[digit_sum].append(n)

        for values in num_sum_map.values():
            if len(values) > 1:
                values.sort(reverse=True)  # Sort in descending order
                max_sum = max(max_sum, values[0] + values[1])

        return max_sum

# Time Complexity: O(nlogn) (worst case), O(n) (best case)
# Space Complexity: O(n)
# check note
