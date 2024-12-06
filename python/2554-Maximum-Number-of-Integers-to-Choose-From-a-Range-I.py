class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        available_options = 0
        currsum = 0
        banned = set(banned) # checks directly in O(1) time by computing a hash

        for num in range(1, n + 1):
            if num in banned:
                continue
            
            if num + currsum > maxSum:
                break
            
            else:
                currsum += num
                available_options += 1
        
        return available_options
                

# time complexity: O(b+n)
# space complexity: O(b)
# check note
