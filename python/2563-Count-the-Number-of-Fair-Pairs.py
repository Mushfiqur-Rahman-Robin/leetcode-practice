class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def bin_search(l, r, target):
            while l <= r:
                mid = (l + r) // 2
                if target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return r

        
        nums.sort()
        r = len(nums) - 1
        num_of_fair_pair = 0

        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]

            num_of_fair_pair += (bin_search(i + 1, r, up + 1) - bin_search(i + 1, r, low))
        
        return num_of_fair_pair


# Time Complexity: O(nlogn)
# Space Complexity: O(1)
# Tutorial link: https://www.youtube.com/watch?v=TjthKf7Mc_8


# num_of_fair_pair = 0 # This code faces TLE

# for i in range(len(nums)):
#     for j in range(1, len(nums)):
#         if nums[i] + nums[j] >= lower and nums[i] + nums[j] <= upper and i < j:
#             num_of_fair_pair += 1

# return num_of_fair_pair
        
