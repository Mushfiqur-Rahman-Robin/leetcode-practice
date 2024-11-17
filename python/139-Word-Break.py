class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp =[False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1): # O(n)
            for w in wordDict: # O(m)
                if i + len(w) <= len(s) and s[i: i+len(w)] == w: # O(k)
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
            
        return dp[0]

# tutorial link: https://www.youtube.com/watch?v=Sx9NNgInc3A
# Time complexity: O(n.m.k)
# Space complexity: O(n)

# check note
