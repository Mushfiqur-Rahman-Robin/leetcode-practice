class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_hashmap = {}
        
        for i, num in enumerate(nums):
            if num in index_hashmap and abs(i - index_hashmap[num]) <= k:
                return True
            
            index_hashmap[num] = i
        
        return False

# time complexity: O(n)
# space complexity: O(n)
# check note
