class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        curr_max = -1
        res = 0

        for idx, num in enumerate(arr):
            curr_max = max(curr_max, num)

            if curr_max == idx:
                res += 1
        
        return res

# tutorial link: https://www.youtube.com/watch?v=wpHzXTkuVkY
# time complexity: O(n)
# space complexity: O(1)
# check note
        
