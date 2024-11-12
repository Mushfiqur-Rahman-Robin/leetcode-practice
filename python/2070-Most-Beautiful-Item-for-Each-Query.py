class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        ans = [0] * len(queries)
        max_beauty = 0
        queries = sorted([(q, i) for i, q in enumerate(queries)])

        j = 0  
        for query, index in queries:
            while j < len(items) and items[j][0] <= query:
                max_beauty = max(max_beauty, items[j][1])
                j += 1

            ans[index] = max_beauty

        return ans
        

# Time Complexity: O(mlogm+nlogn)
# Space Complexity: O(n)
