class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return 
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res
    

# Tutorial link: https://www.youtube.com/watch?v=GBKI9VSKdGg
# Time Complexity: O(2 T), where T is the target.
# Space Complexity: O(T⋅2T), accounting for both recursion depth and result storage.
# Check note
