class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz" 
        }

        res = []
        def backtrack(idx, tmp_res):
            if digits == "":
                return []
            if idx == len(digits):
                res.append(tmp_res[:])
                return
            
            for letter in number_map[digits[idx]]:
                backtrack(idx + 1, tmp_res + letter)
        
        backtrack(0, "")
        return res
            
# time complexity: O(n.k^n)
# space complexity: O(n.k^n)
# check note              
