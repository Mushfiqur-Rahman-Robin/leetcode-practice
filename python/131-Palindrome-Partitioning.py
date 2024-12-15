class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(idx, curr_res):
            if idx == len(s):
                res.append(curr_res[:])
                return
            
            for j in range(idx, len(s)):
                tmp_sol = s[idx: j+1]
                if tmp_sol == tmp_sol[::-1]:
                    backtrack(j + 1, curr_res + [tmp_sol])
        
        backtrack(0, [])
        return res

# time complexity: O(n.2^n)
# space complexity: O(n.2^n)
# check note 
