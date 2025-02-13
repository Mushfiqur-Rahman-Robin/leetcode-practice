class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()

        while len(nums) > 1 and nums[0] < k:
            first = nums.pop(0)
            second = nums.pop(0)
            
            num_to_add = first * 2 + second
            bisect.insort_right(nums, num_to_add)  # Insert in sorted order (O(log n))

            count += 1 

        return count

# time complexity: O(nlogn) # sorting
# space complexity: O(1)
# check note
