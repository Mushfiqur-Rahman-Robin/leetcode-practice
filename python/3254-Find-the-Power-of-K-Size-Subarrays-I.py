class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        consecutive_count = 1

        l = 0
        for r in range(len(nums)):
            if r > 0 and nums[r - 1] + 1 == nums[r]:
                consecutive_count += 1

            if r - l + 1 > k:
                if nums[l] + 1 == nums[l + 1]:
                    consecutive_count -= 1
                l += 1

            if r - l + 1 == k:
                res.append(nums[r] if consecutive_count == k else -1)

        return res
        

# tutorial link: https://www.youtube.com/watch?v=67QUp_zOIFg
# Time complexity: O(n)
# Space complexity: O(1)
