import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)
        
        return min_heap[0]

# tutorial link: https://www.youtube.com/watch?v=ZmGk7h8KZLs
# time complexity: O(nlogk)
# space complexity: O(k)
        