class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return

            if i >= len(candidates) or total > target:
                return 
            
            subset.append(candidates[i])
            dfs(i + 1, subset, total + candidates[i])
            subset.pop()

            # skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, subset, total)
        
        dfs(0, [], 0)
        return res
    
# time complexity: O(nlogn+2^n)
# space complexity: O(n+2^n.k)
# check note
