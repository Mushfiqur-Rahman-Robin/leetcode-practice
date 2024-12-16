class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = - stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)

            if largest != next_largest:
                heapq.heappush(stones, largest - next_largest) # negative -(8 - 7)
        
        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0

# tutorial link: https://www.youtube.com/watch?v=a2dEXlmA1nc
# time complexity: O(nlogn)
# space complexity: O(1)
