class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        tmp = []

        def backtrack(openn, close):
            if len(tmp) == 2 * n:
                ans.append("".join(tmp))
                return 
            
            if openn < n:
                tmp.append("(")
                backtrack(openn + 1, close)
                tmp.pop()
            
            if close < openn:
                tmp.append(")")
                backtrack(openn, close + 1)
                tmp.pop()
        
        backtrack(0, 0)
        return ans

# tutorial link: https://www.youtube.com/watch?v=oC4saZRNwfI
# check note
