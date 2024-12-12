class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            max_gift = max(gifts)
            max_gift_idx = gifts.index(max_gift)
            sqrd_max_gift = int(max_gift ** 0.5)
            gifts[max_gift_idx] = sqrd_max_gift
        
        return sum(gifts)
        
# time complexity: O(k * n)
# space complexity: O(1)
# check note
# potential optimization: use a max heap (priority queue) to reduce time complexity to O(k * log(n))
